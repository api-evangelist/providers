---
aid: kubecost
url: https://raw.githubusercontent.com/api-search/kubecost/refs/heads/main/apis.yml
apis:
  - aid: kubecost:kubecost
    name: Kubecost
    tags:
      - API
    humanURL: ' https://docs.kubecost.com/apis/governance-apis/budget-api'
    properties:
      - url: ' https://docs.kubecost.com/apis/governance-apis/budget-api'
        type: Documentation
    description: |-

      The Budget API allows you to create, update, and delete recurring budget
      rules to control your Kubernetes spending. Weekly and monthly budgets can
      be established on workloads to set limits on cost spend, with the option
      to configure alerts for reaching specified budget thresholds via email,
      Slack, or Microsoft Teams. 
name: Kubecost
tags:
  - Kubernetes
  - Spending
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-13'
modified: '2024-12-30'
position: Consuming
description: |-
  The Budget API allows you to create, update, and delete recurring budget rules
  to control your Kubernetes spending. Weekly and monthly budgets can be
  established on workloads to set limits on cost spend, with the option to
  configure alerts for reaching specified budget thresholds via email, Slack, or
  Microsoft Teams. 
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---