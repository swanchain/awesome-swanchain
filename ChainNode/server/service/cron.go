package service

import (
	"log/slog"
	"os"
	"time"
)

func StartCronService() {
	go ScanChainStatus()
}

const (
	EnvScanDuration = "SCAN_DURATION"
)

const defaultDuration = time.Second * 30

func ScanChainStatus() {
	scanDuration := os.Getenv(EnvScanDuration)
	slog.Info("scan chain", "duration", scanDuration)
	duration := defaultDuration
	if scanDuration != "" {
		sd, err := time.ParseDuration(scanDuration)
		if err != nil {
			slog.Error("parse duration", "failed", err)
		} else {
			duration = sd
		}
	}
	ticker := time.NewTicker(duration)
	for range ticker.C {
		var removeKeys []any
		lotusDataMap.Range(func(key, value any) bool {
			data, ok := value.(*ChainData)
			if ok {
				now := time.Now().Unix()
				since := now - data.ActiveTime
				if since > int64(duration.Seconds()) {
					slog.Info("chain since exceed, need update status", "chain", key, "active time", data.ActiveTime, "since", since)
					data.Status = 0
					if since >= int64(duration.Seconds())*10 {
						slog.Info("chain since exceed max, need remove", "chain", key, "active time", data.ActiveTime, "since", since)
						removeKeys = append(removeKeys, key)
					}
				}
			}
			return true
		})

		for _, key := range removeKeys {
			slog.Info("chain scan remove", "chain", key)
			lotusDataMap.Delete(key)
		}
	}
}