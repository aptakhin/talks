#!/usr/bin/env bash

(cd pdf && rm -rf out/*.pdf && npx playwright test)
