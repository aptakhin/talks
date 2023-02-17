#!/usr/bin/env bash

(cd pdf && rm -rf *.pdf && npx playwright test)
