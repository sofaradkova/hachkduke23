package main

import (
	"log"
	"os"

	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
)

type Config struct {
	// optional default values for the console flags
	DefaultDebug         bool
	DefaultDataDir       string // if not set, it will fallback to "./pb_data"
	DefaultEncryptionEnv string

	// hide the default console server info on app startup
	HideStartBanner bool

	// optional DB configurations
	DataMaxOpenConns int // default to core.DefaultDataMaxOpenConns
	DataMaxIdleConns int // default to core.DefaultDataMaxIdleConns
	LogsMaxOpenConns int // default to core.DefaultLogsMaxOpenConns
	LogsMaxIdleConns int // default to core.DefaultLogsMaxIdleConns
}

func main() {
    app := pocketbase.New()

    // serves static files from the provided public dir (if exists)
    app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
        e.Router.GET("/*", apis.StaticDirectoryHandler(os.DirFS("./pb_public"), false))
        return nil
    })

    if err := app.Start(); err != nil {
        log.Fatal(err)
    }
}