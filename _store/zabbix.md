---
aid: zabbix
name: Zabbix
description: Zabbix is an enterprise-class open source distributed monitoring solution for networks and applications. Zabbix enables real-time monitoring of millions of metrics collected from tens of thousands of servers, virtual machines, and network devices. The Zabbix API provides JSON-RPC 2.0 access for programmatically managing host configurations, collecting monitoring data, and automating operations.
image: https://www.zabbix.com/assets/img/logo/zabbix_logo.png
url: https://raw.githubusercontent.com/api-evangelist/zabbix/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Monitoring
  - Infrastructure
  - Networks
  - Alerting
  - Open Source
  - Observability
apis:
  - aid: zabbix:zabbix-api
    name: Zabbix API
    description: The Zabbix API is a JSON-RPC 2.0 HTTP API for programmatically retrieving and modifying the configuration of Zabbix and accessing historical monitoring data. Supports host management, item configuration, trigger management, event handling, alerting, user management, and historical data retrieval.
    image: https://www.zabbix.com/assets/img/logo/zabbix_logo.png
    humanURL: https://www.zabbix.com/documentation/current/en/manual/api
    baseURL: https://{host}/zabbix/api_jsonrpc.php
    tags:
      - Monitoring
      - Infrastructure
      - JSON-RPC
      - Alerting
      - Networks
    properties:
      - type: Documentation
        url: https://www.zabbix.com/documentation/current/en/manual/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/zabbix/refs/heads/main/openapi/zabbix-openapi.yml
      - type: GettingStarted
        url: https://www.zabbix.com/documentation/current/en/manual/quickstart
      - type: Authentication
        url: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/login
      - type: ChangeLog
        url: https://www.zabbix.com/documentation/current/en/manual/introduction/whatsnew
    contact:
      - type: Support
        url: https://www.zabbix.com/support
      - type: Forum
        url: https://www.zabbix.com/forum
      - type: Email
        url: mailto:sales@zabbix.com
common:
  - type: Portal
    url: https://www.zabbix.com
  - type: Blog
    url: https://blog.zabbix.com
  - type: GitHub
    url: https://github.com/zabbix/zabbix
  - type: GitHubOrg
    url: https://github.com/zabbix
  - type: Docker
    url: https://github.com/zabbix/zabbix-docker
  - type: AnsibleCollection
    url: https://github.com/zabbix/ansible-collection
  - type: CommunityTemplates
    url: https://github.com/zabbix/community-templates
  - type: Twitter
    url: https://twitter.com/zabbix
  - type: PrivacyPolicy
    url: https://www.zabbix.com/privacy_policy
  - type: TermsOfService
    url: https://www.zabbix.com/terms_of_use
  - type: Download
    url: https://www.zabbix.com/download
  - type: Integrations
    data:
      - name: Ansible Collection
      - name: Docker / Kubernetes
      - name: Grafana Plugin
      - name: Slack Notifications
      - name: PagerDuty Integration
      - name: Jira Integration
      - name: ServiceNow Integration
  - type: Features
    data:
      - name: Host Monitoring
      - name: Network Monitoring
      - name: Application Monitoring
      - name: Cloud Monitoring
      - name: Agent-Based Collection
      - name: Agentless Collection (SNMP, IPMI, JMX)
      - name: Triggers and Alerting
      - name: Dashboards and Visualizations
      - name: Historical Data Storage
      - name: Scalable Distributed Monitoring
      - name: Auto Discovery
      - name: API Automation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
