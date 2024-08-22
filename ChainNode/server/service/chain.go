package service

import (
	"errors"
	"sort"
	"strings"
)

type ChainService struct{}

func (s *ChainService) Report(data *ChainData) error {
	if data.URL == "" || data.URL == "https://" {
		return errors.New("invalid URL parameter")
	}
	if !strings.HasPrefix(data.URL, "https://") {
		data.URL = "https://" + data.URL
	}
	lotusDataMap.Store(data.URL, data)
	return nil
}

func (s *ChainService) List(id string) (list []*ChainData, err error) {
	lotusDataMap.Range(func(key, value any) bool {
		data, ok := value.(*ChainData)
		if ok {
			if id == "" {
				list = append(list, data)
			} else {
				if data.ChainID == id {
					list = append(list, data)
				}
			}
		}
		return true
	})
	sort.Slice(list, func(i, j int) bool {
		if list[i].Status > list[j].Status {
			return true
		}
		return list[i].URL < list[j].URL
	})
	return
}

func (s *ChainService) ListChain() (list []*ChainData, err error) {
	m := make(map[string]*ChainData)
	lotusDataMap.Range(func(key, value any) bool {
		data, ok := value.(*ChainData)
		if ok {
			m[data.ChainID] = data
		}
		return true
	})
	for _, data := range m {
		list = append(list, data)
	}
	sort.Slice(list, func(i, j int) bool {
		if list[i].Chain < list[j].Chain {
			return true
		}
		return list[i].Net < list[j].Net
	})
	return
}
