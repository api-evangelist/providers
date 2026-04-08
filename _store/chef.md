---
aid: chef
url: https://raw.githubusercontent.com/api-evangelist/chef/refs/heads/main/apis.yml
apis:
- aid: chef:chef-infra-server-api
  name: Chef Infra Server API
  tags:
  - Configuration Management
  - Infrastructure
  humanURL: https://docs.chef.io/server/api_chef_server/
  properties:
  - url: https://docs.chef.io/server/api_chef_server/
    type: Documentation
  description: REST API for managing nodes, cookbooks, roles, environments, and other Chef Infra objects.
- aid: chef:chef-automate-api
  name: Chef Automate API
  tags:
  - Automation
  - Compliance
  humanURL: https://docs.chef.io/automate/api/
  properties:
  - url: https://docs.chef.io/automate/api/
    type: Documentation
  - url: https://docs.chef.io/automate/api_swagger/
    type: Reference
  description: API for Chef Automate providing visibility into infrastructure, compliance, and application deployment.
name: Chef
tags:
- Automation
- Compliance
- Configuration Management
- DevOps
- Infrastructure as Code
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Chef (Progress Chef) provides a collection of APIs for infrastructure automation, compliance, and application delivery. Chef enables organizations to automate infrastructure configuration, compliance testing, and application deployment workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

