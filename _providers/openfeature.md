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
  try_now: true
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Openfeature Agentic Access
  operation_count: 2
  slug: openfeature-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: '**Required**: Core APIs to implement to support OFREP. *This is the minimum set of APIs required for a flag management system to be OFREP compatible.*'
  name: OpenFeature OFREP Core API
  slug: openfeature-ofrep-core-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFeature Remote Evaluation Protocol (OFREP) OFREP Core API
  slug: open-openfeature-ofrep-core-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.openfeature.dev/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openfeature-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openfeature-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openfeature-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openfeature
- group: docs
  title: ''
  type: Documentation
  url: https://openfeature.dev/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/open-feature
- group: company
  title: ''
  type: Blog
  url: https://openfeature.dev/blog/rss.xml
created: '2026-03-16'
description: OpenFeature is a CNCF incubating open specification for feature flag management. It provides a vendor-agnostic API for evaluating feature flags, enabling developers to use a consistent interface regardless of the underlying feature flag provider. OpenFeature offers SDKs in multiple languages including Go, Java, JavaScript, Python, PHP, and .NET with a provider-based architecture.
finops:
- name: Openfeature Finops
  service_category: API
  slug: openfeature-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openfeature.png
layout: provider
modified: '2026-05-19'
name: OpenFeature
nav: Providers
network: true
overview: 'OpenFeature publishes 1 API on the [APIs.io](https://apis.io/) network: OFREP Core API. Tagged areas include Cloud-Native, Feature Flags, Feature Management, Incubating, and SDK.


  OpenFeature''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Openfeature Plans Pricing
  plan_count: 3
  slug: openfeature-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Openfeature Rate Limits
  slug: openfeature-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/openfeature/refs/heads/main/screenshots/openfeature-2026-06-20T191000.png
security:
- kind: authentication
  name: Openfeature Authentication
  slug: openfeature-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Openfeature Domain Security
  slug: openfeature-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openfeature
tags:
- Cloud-Native
- Feature Flags
- Feature Management
- Incubating
- SDK
- Specification
website: https://www.openfeature.dev/
---
