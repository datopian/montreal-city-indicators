'use strict'

const nconf = require('nconf')
require('dotenv').config()

nconf.argv()
  .env()

const api_url = process.env.API_URL || 'http://127.0.0.1:5000/api/3/action/'

// This is the object that you want to override in your own local config
nconf.defaults({
  env: process.env.NODE_ENV || 'development',
  debug: process.env.DEBUG || false,
  app: {
    port: process.env.PORT || 4000
  },
  API_URL: api_url,
  SITE_URL: process.env.SITE_URL || 'http://0.0.0.0:4000',
  WP_URL: process.env.WP_URL || 'http://127.0.0.1:6000',
  THEME_DIR: process.env.THEME_DIR || 'themes'
})

module.exports = {
  get: nconf.get.bind(nconf),
  set: nconf.set.bind(nconf),
  reset: nconf.reset.bind(nconf)
}
