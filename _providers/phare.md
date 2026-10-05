---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Phare Agentic Access
  operation_count: 48
  slug: phare-agentic-access
  summary_line: 48 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Alert Rules
  name: Phare Alert Rules API
  slug: phare-alert-rules-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Incidents
  name: Phare Incidents API
  slug: phare-incidents-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Integrations
  name: Phare Integrations API
  slug: phare-integrations-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Maintenance Windows
  name: Phare Maintenance Windows API
  slug: phare-maintenance-windows-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Monitors
  name: Phare Monitors API
  slug: phare-monitors-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Platform
  name: Phare Platform API
  slug: phare-platform-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Projects
  name: Phare Projects API
  slug: phare-projects-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Reports
  name: Phare Reports API
  slug: phare-reports-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Status Pages
  name: Phare Status Pages API
  slug: phare-status-pages-api
- baseURL: https://api.phare.io
  baseurl_source: declared
  description: Users
  name: Phare Users API
  slug: phare-users-api
artifact_total: 24
asyncapis:
- description: ''
  name: Phare Webhooks
  slug: phare-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/capabilities/phare-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/phare-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/agentic-access/phare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/phare-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/plans/phare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phare-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/rules/phare-rules.yml
  title: ''
  type: Spectral
  url: rules/phare-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/json-ld/phare-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/phare-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/vocabulary/phare-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/phare-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/asyncapi/phare-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/phare-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/data-model/phare-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phare-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/changelog/phare-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/phare-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://phare.io/legal/vulnerability-disclosure
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/errors/phare-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/phare-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/conformance/phare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phare-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/llms/phare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phare-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/a2a/phare-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/phare-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/well-known/phare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/phare-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/well-known/phare-pushover-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/phare-pushover-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/well-known/phare-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/phare-app-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/well-known/phare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phare-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/hosts/phare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/vendors/phare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phare-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phare.io/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.phare.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phare.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phare
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.phare.io/changelog/platform/2026
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phare.io/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.phare.io/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/authentication/phare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phare-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/security/phare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/phare-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phare/refs/heads/main/security/phare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phare.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.phare.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phare.io/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://phare.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://phare.io/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.phare.io/register
created: '2026-09-27'
description: Phare provides European uptime monitoring, incident management, and analytics solutions. Their platform offers real‑time website and server uptime checks, customizable alerts, AI‑assisted incident handling, and privacy‑first analytics without cookies. Users can create status pages, integrate with various services, and access detailed traffic insights, all tailored for European compliance and reliability.
image: https://phare.io/img/open-graph.jpg
json_schemas:
- name: links
  property_count: 4
  slug: phare-links
- name: meta
  property_count: 5
  slug: phare-meta
- name: Outgoing Webhooks
  property_count: 1
  slug: phare-platform-app-outgoing-webhook-alert-rule-settings
- name: Pushover
  property_count: 3
  slug: phare-platform-app-pushover-alert-rule-settings
- name: Uptime certificate expiring
  property_count: 1
  slug: phare-platform-event-uptime-monitor-certificate-expiring-alert-rule-settings
- name: Uptime.ProductEvents
  property_count: 0
  slug: phare-uptime-product-events
jsonld:
- class_count: 21
  name: Phare Context
  property_count: 14
  slug: phare-context
layout: provider
modified: '2026-09-27'
name: Phare
nav: Providers
network: true
overview: 'Phare publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alert Rules API, Incidents API, Integrations API, and 7 more. Tagged areas include Company, Monitoring, Incident Management, Analytics, and European.


  The Phare catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Phare''s developer surface includes changelog, getting-started guide, API reference, authentication, documentation, pricing, engineering blog, and 30 more developer resources.'
plans:
- name: Phare Plans Pricing
  plan_count: 2
  slug: phare-plans-pricing
random_paper: 0
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Phare API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: phare-rules
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 77.2
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Phare Authentication
  slug: phare-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Phare Domain Security
  slug: phare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Phare Vulnerability Disclosure
  slug: phare-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: phare
tags:
- Company
- Monitoring
- Incident Management
- Analytics
- European
website: https://phare.io/
---
