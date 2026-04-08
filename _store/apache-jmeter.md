---
aid: apache-jmeter
url: https://raw.githubusercontent.com/api-evangelist/apache-jmeter/refs/heads/main/apis.yml
apis:
- name: JMeter REST API
  description: RESTful API for controlling and monitoring JMeter tests remotely.
  image: https://jmeter.apache.org/images/logo.svg
  humanURL: https://jmeter.apache.org/
  baseURL: http://localhost:8080/api
  tags:
  - Performance
  - Rest
  - Testing
  properties:
  - type: Documentation
    url: https://jmeter.apache.org/usermanual/remote-test.html
  - type: OpenAPI
    url: https://jmeter-plugins.org/wiki/HttpSimpleTableServer/
  - type: Swagger
    url: http://localhost:8080/api/swagger-ui.html
  contact:
  - FN: Apache JMeter Project
    email: dev@jmeter.apache.org
    url: https://jmeter.apache.org/mail.html
- name: JMeter CLI Interface
  description: Command-line interface for running JMeter tests in non-GUI mode.
  humanURL: https://jmeter.apache.org/usermanual/get-started.html#non_gui
  baseURL: command-line
  tags:
  - Automation
  - Cli
  - Command-Line
  properties:
  - type: Documentation
    url: https://jmeter.apache.org/usermanual/get-started.html#non_gui
  - type: User Manual
    url: https://jmeter.apache.org/usermanual/
- name: JMeter Plugins Manager API
  description: API for managing JMeter plugins programmatically.
  humanURL: https://jmeter-plugins.org/
  baseURL: https://jmeter-plugins.org/
  tags:
  - Extensions
  - Plugins
  properties:
  - type: Documentation
    url: https://jmeter-plugins.org/wiki/PluginsManager/
  - type: GitHub
    url: https://github.com/undera/jmeter-plugins-manager
name: Apache JMeter
tags:
- Api Testing
- Load Testing
- Open Source
- Performance Testing
- Stress Testing
type: Contract
image: https://jmeter.apache.org/images/logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache JMeter is an open source software designed to load test functional behavior and measure performance. It was originally designed for testing Web Applications but has since expanded to other test functions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

