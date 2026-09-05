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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 119
  human_in_the_loop: 0
  name: Influxdb Agentic Access
  operation_count: 194
  slug: influxdb-agentic-access
  summary_line: 194 operations · 119 acting
api_count: 1
apis:
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Create and manage authorizations (API tokens). An _authorization_ contains a list of `read` and `write` permissions for organization resources and provides an API token for authentication. An authoriz
  name: InfluxDB Authorizations (API tokens) API
  slug: influxdb-authorizations-api-tokens-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Bucket Schemas API from InfluxDB — 2 operation(s) for bucket schemas.
  name: InfluxDB Bucket Schemas API
  slug: influxdb-bucket-schemas-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Store your data in InfluxDB [buckets](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#bucket). A bucket is a named location where time series data is stored. All buckets have a [retenti
  name: InfluxDB Buckets API
  slug: influxdb-buckets-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Cells API from InfluxDB — 3 operation(s) for cells.
  name: InfluxDB Cells API
  slug: influxdb-cells-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Checks API from InfluxDB — 5 operation(s) for checks.
  name: InfluxDB Checks API
  slug: influxdb-checks-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Config API from InfluxDB — 1 operation(s) for config.
  name: InfluxDB Config API
  slug: influxdb-config-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Dashboards API from InfluxDB — 11 operation(s) for dashboards.
  name: InfluxDB Dashboards API
  slug: influxdb-dashboards-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Data I/O endpoints API from InfluxDB — 9 operation(s) for data i/o endpoints.
  name: InfluxDB Data I/O endpoints API
  slug: influxdb-data-i-o-endpoints-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The InfluxDB 1.x data model includes [databases](https://docs.influxdata.com/influxdb/v1.8/concepts/glossary/#database) and [retention policies](https://docs.influxdata.com/influxdb/v1.8/concepts/glos
  name: InfluxDB DBRPs API
  slug: influxdb-dbrps-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Delete data from an InfluxDB bucket.
  name: InfluxDB Delete API
  slug: influxdb-delete-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: 'Store, manage, and execute scripts in InfluxDB. A script stores your custom Flux script and provides an invokable endpoint that accepts runtime parameters. In a script, you can specify custom runtime '
  name: InfluxDB Invokable Scripts API
  slug: influxdb-invokable-scripts-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Labels API from InfluxDB — 2 operation(s) for labels.
  name: InfluxDB Labels API
  slug: influxdb-labels-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Legacy Authorizations API from InfluxDB — 3 operation(s) for legacy authorizations.
  name: InfluxDB Legacy Authorizations API
  slug: influxdb-legacy-authorizations-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Legacy Query API from InfluxDB — 1 operation(s) for legacy query.
  name: InfluxDB Legacy Query API
  slug: influxdb-legacy-query-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Legacy Write API from InfluxDB — 1 operation(s) for legacy write.
  name: InfluxDB Legacy Write API
  slug: influxdb-legacy-write-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Limits API from InfluxDB — 1 operation(s) for limits.
  name: InfluxDB Limits API
  slug: influxdb-limits-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Maps API from InfluxDB — 1 operation(s) for maps.
  name: InfluxDB Maps API
  slug: influxdb-maps-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The NotificationEndpoints API from InfluxDB — 4 operation(s) for notificationendpoints.
  name: InfluxDB NotificationEndpoints API
  slug: influxdb-notificationendpoints-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The NotificationRules API from InfluxDB — 4 operation(s) for notificationrules.
  name: InfluxDB NotificationRules API
  slug: influxdb-notificationrules-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Manage your [organization](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#organization). An organization is a workspace for a group of users. Organizations can be used to separate diff
  name: InfluxDB Organizations API
  slug: influxdb-organizations-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Ping API from InfluxDB — 1 operation(s) for ping.
  name: InfluxDB Ping API
  slug: influxdb-ping-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Retrieve data, analyze queries, and get query suggestions.
  name: InfluxDB Query API
  slug: influxdb-query-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Resources API from InfluxDB — 1 operation(s) for resources.
  name: InfluxDB Resources API
  slug: influxdb-resources-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Routes API from InfluxDB — 1 operation(s) for routes.
  name: InfluxDB Routes API
  slug: influxdb-routes-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Rules API from InfluxDB — 1 operation(s) for rules.
  name: InfluxDB Rules API
  slug: influxdb-rules-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Secrets API from InfluxDB — 3 operation(s) for secrets.
  name: InfluxDB Secrets API
  slug: influxdb-secrets-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Security and access endpoints API from InfluxDB — 15 operation(s) for security and access endpoints.
  name: InfluxDB Security and access endpoints API
  slug: influxdb-security-and-access-endpoints-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Setup API from InfluxDB — 2 operation(s) for setup.
  name: InfluxDB Setup API
  slug: influxdb-setup-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Signin API from InfluxDB — 1 operation(s) for signin.
  name: InfluxDB Signin API
  slug: influxdb-signin-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Signout API from InfluxDB — 1 operation(s) for signout.
  name: InfluxDB Signout API
  slug: influxdb-signout-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The System information endpoints API from InfluxDB — 3 operation(s) for system information endpoints.
  name: InfluxDB System information endpoints API
  slug: influxdb-system-information-endpoints-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Process and analyze your data with [tasks](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#task) in the InfluxDB task engine. Use the `/api/v2/tasks` endpoints to schedule and manage ta
  name: InfluxDB Tasks API
  slug: influxdb-tasks-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Telegraf Plugins API from InfluxDB — 1 operation(s) for telegraf plugins.
  name: InfluxDB Telegraf Plugins API
  slug: influxdb-telegraf-plugins-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Telegrafs API from InfluxDB — 8 operation(s) for telegrafs.
  name: InfluxDB Telegrafs API
  slug: influxdb-telegrafs-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Export and apply InfluxDB **templates**. Manage **stacks** of templated InfluxDB resources. InfluxDB templates are prepackaged configurations for resources. Use InfluxDB templates to configure a fresh
  name: InfluxDB Templates API
  slug: influxdb-templates-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Usage API from InfluxDB — 1 operation(s) for usage.
  name: InfluxDB Usage API
  slug: influxdb-usage-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Retrieve specific users. InfluxDB Cloud lets you invite and collaborate with multiple users in your organization. To invite and remove users from your organization, use the InfluxDB Cloud user interfa
  name: InfluxDB Users API
  slug: influxdb-users-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Variables API from InfluxDB — 4 operation(s) for variables.
  name: InfluxDB Variables API
  slug: influxdb-variables-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: The Views API from InfluxDB — 1 operation(s) for views.
  name: InfluxDB Views API
  slug: influxdb-views-api
- baseURL: https://cloud2.influxdata.com/api/v2
  baseurl_source: declared
  description: Write time series data to [buckets](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#bucket).
  name: InfluxDB Write API
  slug: influxdb-write-api
artifact_total: 91
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: InfluxDB Notification Endpoints and Write Surfaces
  slug: open-influxdb-asyncapi
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Authorizations (API tokens) API
  slug: open-influxdb-authorizations-api-tokens-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Bucket Schemas API
  slug: open-influxdb-bucket-schemas-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Buckets API
  slug: open-influxdb-buckets-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Cells API
  slug: open-influxdb-cells-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Checks API
  slug: open-influxdb-checks-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Config API
  slug: open-influxdb-config-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Dashboards API
  slug: open-influxdb-dashboards-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Data I/O endpoints API
  slug: open-influxdb-data-i-o-endpoints-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) DBRPs API
  slug: open-influxdb-dbrps-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Delete API
  slug: open-influxdb-delete-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Invokable Scripts API
  slug: open-influxdb-invokable-scripts-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Labels API
  slug: open-influxdb-labels-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Legacy Authorizations API
  slug: open-influxdb-legacy-authorizations-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Legacy Query API
  slug: open-influxdb-legacy-query-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Legacy Write API
  slug: open-influxdb-legacy-write-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Limits API
  slug: open-influxdb-limits-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Maps API
  slug: open-influxdb-maps-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) NotificationEndpoints API
  slug: open-influxdb-notificationendpoints-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) NotificationRules API
  slug: open-influxdb-notificationrules-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Organizations API
  slug: open-influxdb-organizations-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Ping API
  slug: open-influxdb-ping-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Query API
  slug: open-influxdb-query-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Resources API
  slug: open-influxdb-resources-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Routes API
  slug: open-influxdb-routes-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Rules API
  slug: open-influxdb-rules-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Secrets API
  slug: open-influxdb-secrets-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Security and access endpoints API
  slug: open-influxdb-security-and-access-endpoints-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Setup API
  slug: open-influxdb-setup-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Signin API
  slug: open-influxdb-signin-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Signout API
  slug: open-influxdb-signout-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) System information endpoints API
  slug: open-influxdb-system-information-endpoints-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Tasks API
  slug: open-influxdb-tasks-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Telegraf Plugins API
  slug: open-influxdb-telegraf-plugins-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Telegrafs API
  slug: open-influxdb-telegrafs-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Templates API
  slug: open-influxdb-templates-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Usage API
  slug: open-influxdb-usage-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Users API
  slug: open-influxdb-users-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Variables API
  slug: open-influxdb-variables-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Views API
  slug: open-influxdb-views-api
- collection_type: open
  name: Complete InfluxDB Cloud Authorizations (API tokens) Authorizations (API tokens) Write API
  slug: open-influxdb-write-api
- collection_type: open
  name: Complete InfluxDB Cloud API
  slug: open-influxdb
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/influxdb-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/influxdb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/influxdb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/influxdb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/influxdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/influxdb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.influxdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.influxdata.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.influxdata.com/influxdb/cloud/api/v2/#tag/Quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://www.influxdata.com/influxdb-pricing/
- group: other
  title: ''
  type: Resources
  url: https://www.influxdata.com/_resources/?pg=1
- group: learn
  title: ''
  type: Webinars
  url: https://www.influxdata.com/_resources/?pg=1&ct=webinar
- group: other
  title: ''
  type: White Papers
  url: https://www.influxdata.com/_resources/?pg=1&ct=tech_paper
- group: learn
  title: ''
  type: Video
  url: https://www.influxdata.com/_resources/?pg=1&ct=video
- group: other
  title: ''
  type: Case Studies
  url: https://www.influxdata.com/_resources/?pg=1&ct=case_study
- group: other
  title: ''
  type: Events
  url: https://www.influxdata.com/events/
- group: other
  title: ''
  type: Glossary
  url: https://www.influxdata.com/glossary/
- group: operate
  title: ''
  type: Issues
  url: https://github.com/influxdata/influxdb/issues/new/choose/
- group: operate
  title: ''
  type: Support
  url: https://support.influxdata.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/influxdata/influxdb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/influxdb/
created: '2024-09-25'
description: InfluxData is the company building InfluxDB, the open source time series database used by more than a million developers around the world. Their mission is to help developers build intelligent, real-time systems with their time series data, with offerings spanning open source InfluxDB Core and Enterprise, InfluxDB Cloud Serverless and Dedicated, and Telegraf for data collection.
finops:
- name: Influxdb Finops
  service_category: API
  slug: influxdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/influxdb.png
layout: provider
modified: '2026-05-30'
name: InfluxDB
nav: Providers
network: true
overview: 'InfluxDB publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Authorizations (API tokens) API, Bucket Schemas API, Buckets API, and 37 more. Tagged areas include Database, Time Series, Real-Time, and Analytics.


  InfluxDB''s developer surface includes authentication, documentation, getting-started guide, pricing, support, GitHub presence, and 15 more developer resources.'
plans:
- name: Influxdb Plans Pricing
  plan_count: 3
  slug: influxdb-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Influxdb Rate Limits
  slug: influxdb-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 53.5
    developer_ergonomics: 23.8
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 2.4
      derived: 0
      marker_coverage: 0.0
      total: 41
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/influxdb/refs/heads/main/screenshots/influxdb-2026-06-20T183337.png
security:
- kind: authentication
  name: Influxdb Authentication
  slug: influxdb-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Influxdb Domain Security
  slug: influxdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Influxdb Vulnerability Disclosure
  slug: influxdb-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Influxdb Trust Center
  slug: influxdb-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018
slug: influxdb
tags:
- Database
- Time Series
- Real-Time
- Analytics
website: https://www.influxdata.com/
---
