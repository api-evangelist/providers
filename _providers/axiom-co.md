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
- acting_count: 31
  human_in_the_loop: 0
  name: Axiom Co Agentic Access
  operation_count: 56
  slug: axiom-co-agentic-access
  summary_line: 56 operations · 31 acting
api_count: 1
apis:
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Mark deployments, incidents, and events on charts.
  name: Axiom Annotations API
  slug: axiom-co-annotations-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Collections of charts and visualizations.
  name: Axiom Dashboards API
  slug: axiom-co-dashboards-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Manage the datasets that store ingested event data.
  name: Axiom Datasets API
  slug: axiom-co-datasets-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Inspect and annotate dataset fields.
  name: Axiom Fields API
  slug: axiom-co-fields-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Send logs, traces, and events into a dataset.
  name: Axiom Ingest API
  slug: axiom-co-ingest-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: APL-backed alert monitors.
  name: Axiom Monitors API
  slug: axiom-co-monitors-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Notification channels monitors dispatch through.
  name: Axiom Notifiers API
  slug: axiom-co-notifiers-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Organization-level settings.
  name: Axiom Organizations API
  slug: axiom-co-organizations-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Run APL queries across datasets.
  name: Axiom Query API
  slug: axiom-co-query-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Saved, shareable APL queries.
  name: Axiom Starred Queries API
  slug: axiom-co-starred-queries-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Scoped API tokens used to authenticate requests.
  name: Axiom Tokens API
  slug: axiom-co-tokens-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Current user and organization members.
  name: Axiom Users API
  slug: axiom-co-users-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Derived fields computed from an APL expression at query time.
  name: Axiom Virtual Fields API
  slug: axiom-co-virtual-fields-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Axiom Annotations API
  slug: open-axiom-co-annotations-api
- collection_type: open
  name: Axiom Annotations Dashboards API
  slug: open-axiom-co-dashboards-api
- collection_type: open
  name: Axiom Annotations Datasets API
  slug: open-axiom-co-datasets-api
- collection_type: open
  name: Axiom Annotations Fields API
  slug: open-axiom-co-fields-api
- collection_type: open
  name: Axiom Annotations Ingest API
  slug: open-axiom-co-ingest-api
- collection_type: open
  name: Axiom Annotations Monitors API
  slug: open-axiom-co-monitors-api
- collection_type: open
  name: Axiom Annotations Notifiers API
  slug: open-axiom-co-notifiers-api
- collection_type: open
  name: Axiom Annotations Organizations API
  slug: open-axiom-co-organizations-api
- collection_type: open
  name: Axiom Annotations Query API
  slug: open-axiom-co-query-api
- collection_type: open
  name: Axiom Annotations Starred Queries API
  slug: open-axiom-co-starred-queries-api
- collection_type: open
  name: Axiom Annotations Tokens API
  slug: open-axiom-co-tokens-api
- collection_type: open
  name: Axiom Annotations Users API
  slug: open-axiom-co-users-api
- collection_type: open
  name: Axiom Annotations Virtual Fields API
  slug: open-axiom-co-virtual-fields-api
- collection_type: open
  name: Axiom API
  slug: open-axiom-co
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/axiom-co-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axiom-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/axiom-co-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axiomhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axiomhq
- group: company
  title: ''
  type: Website
  url: https://axiom.co/
- group: docs
  title: ''
  type: Documentation
  url: https://axiom.co/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/axiom-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/axiom-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/axiom-co-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://axiom.co/blog/feed.xml
created: '2026-07-02'
description: Axiom is a log management, event data, and observability platform that ingests, stores, and queries large volumes of logs, traces, and events at low cost. Data is loaded into datasets and queried with the Axiom Processing Language (APL). The REST API (base https://api.axiom.co, US region; https://api.eu.axiom.co for EU) exposes ingest, APL query, datasets, fields, annotations, monitors, notifiers, dashboards, virtual fields, starred queries, API tokens, users, and organizations, with v1 and v2 endpoint families and Bearer token authentication.
finops:
- name: Axiom Co Finops
  service_category: Observability and Log Management
  slug: axiom-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axiom-co.png
layout: provider
modified: '2026-07-02'
name: Axiom
nav: Providers
network: true
overview: 'Axiom publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, Dashboards API, Datasets API, and 10 more. Tagged areas include Observability, Log Management, Event Data, Logs, and Tracing.


  Axiom''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Axiom Co Plans Pricing
  plan_count: 3
  slug: axiom-co-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Axiom Co Rate Limits
  slug: axiom-co-rate-limits
security:
- kind: authentication
  name: Axiom Co Authentication
  slug: axiom-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Axiom Co Domain Security
  slug: axiom-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axiom-co
tags:
- Observability
- Log Management
- Event Data
- Logs
- Tracing
- Analytics
- APL
website: https://axiom.co/
---
