---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Nacos Agentic Access
  operation_count: 26
  slug: nacos-agentic-access
  summary_line: 26 operations · 16 acting
api_count: 1
apis:
- baseURL: http://localhost:8848/nacos
  baseurl_source: declared
  description: Authentication
  name: Nacos Auth API
  slug: nacos-auth-api
- baseURL: http://localhost:8848/nacos
  baseurl_source: declared
  description: Configuration management operations
  name: Nacos Configuration API
  slug: nacos-configuration-api
- baseURL: http://localhost:8848/nacos
  baseurl_source: declared
  description: Namespace management
  name: Nacos Namespace API
  slug: nacos-namespace-api
- baseURL: http://localhost:8848/nacos
  baseurl_source: declared
  description: Server operations and metrics
  name: Nacos Operator API
  slug: nacos-operator-api
- baseURL: http://localhost:8848/nacos
  baseurl_source: declared
  description: Service instance registration and discovery
  name: Nacos Service Discovery API
  slug: nacos-service-discovery-api
- baseURL: http://localhost:8848/nacos
  baseurl_source: declared
  description: Service definition management
  name: Nacos Service Management API
  slug: nacos-service-management-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nacos Open Auth API
  slug: open-nacos-auth-api
- collection_type: open
  name: Nacos Open Auth Configuration API
  slug: open-nacos-configuration-api
- collection_type: open
  name: Nacos Open Auth Namespace API
  slug: open-nacos-namespace-api
- collection_type: open
  name: Nacos Open API
  slug: open-nacos-open-api
- collection_type: open
  name: Nacos Open Auth Operator API
  slug: open-nacos-operator-api
- collection_type: open
  name: Nacos Open Auth Service Discovery API
  slug: open-nacos-service-discovery-api
- collection_type: open
  name: Nacos Open Auth Service Management API
  slug: open-nacos-service-management-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nacos-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nacos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nacos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nacos-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nacos.io/
- group: docs
  title: ''
  type: Documentation
  url: https://nacos.io/docs/latest/what-is-nacos/
- group: start
  title: ''
  type: GettingStarted
  url: https://nacos.io/docs/latest/quickstart/quick-start/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alibaba/nacos
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/alibaba
- group: company
  title: ''
  type: Blog
  url: https://nacos.io/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/alibaba/nacos/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/alibaba/nacos/issues
created: '2026-03-26'
description: Nacos is an easy-to-use dynamic service discovery, configuration, and service management platform from Alibaba for building cloud-native applications, supporting Dubbo, gRPC, Spring Cloud RESTful, and Kubernetes services.
finops:
- name: Nacos Finops
  service_category: API
  slug: nacos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nacos.png
layout: provider
modified: '2026-05-19'
name: Nacos
nav: Providers
network: true
overview: 'Nacos publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Configuration API, Namespace API, and 3 more. Tagged areas include Alibaba, Cloud-Native, Configuration Management, DNS, and Java.


  Nacos'' developer surface includes authentication, documentation, getting-started guide, GitHub presence, engineering blog, release notes, and 6 more developer resources.'
plans:
- name: Nacos Plans Pricing
  plan_count: 3
  slug: nacos-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Nacos Rate Limits
  slug: nacos-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/nacos/refs/heads/main/screenshots/nacos-2026-06-20T185930.png
security:
- kind: authentication
  name: Nacos Authentication
  slug: nacos-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nacos Domain Security
  slug: nacos-domain-security
  summary_line: TLSv1.3
slug: nacos
tags:
- Alibaba
- Cloud-Native
- Configuration Management
- DNS
- Java
- Microservices
- Service Discovery
- Service Management
website: https://nacos.io/
---
