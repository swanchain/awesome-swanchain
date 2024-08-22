package result

type Result struct {
	Code int    `json:"code"`
	Msg  string `json:"msg"`
	Data any    `json:"data,omitempty"`
}

const (
	Success         = 0
	DBError         = 1001
	RedisError      = 1002
	FileCreateError = 1003
	ServerError     = 1004

	InvalidPara = 1101
	URLInvalid  = 1102

	UserEmailRegistered  = 1201
	UserEmailCodeInvalid = 1202
	UserEmailSendFailed  = 1203
	UserTokenInvalid     = 1204
	UserTokenExpired     = 1205
	UserNotFound         = 1206

	UserEmailPasswordIncorrect = 1301

	DatasetNotFound = 2001
	DatasetRepeat   = 2002

	FileNotFound = 2101
	FileNotMatch = 2102

	DownloadLinkError = 2201

	ServicePackageNotFound      = 3001
	ServicePackageSizeNotEnough = 3002

	AppRepeat   = 4001
	AppNotFound = 4002

	IpfsUploadError = 5001
	BackupError     = 5002
)
