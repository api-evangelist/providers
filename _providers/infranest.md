---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 102
  human_in_the_loop: 15
  name: Infranest Agentic Access
  operation_count: 360
  slug: infranest-agentic-access
  summary_line: 360 operations · 102 acting · 15 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Audit Log API from InfraNest — 2 operation(s) for audit log.
  name: InfraNest Audit Log API
  slug: infranest-audit-log-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Authentication API from InfraNest — 2 operation(s) for authentication.
  name: InfraNest Authentication API
  slug: infranest-authentication-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Automations API from InfraNest — 8 operation(s) for automations.
  name: InfraNest Automations API
  slug: infranest-automations-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Billing API from InfraNest — 7 operation(s) for billing.
  name: InfraNest Billing API
  slug: infranest-billing-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Certificates API from InfraNest — 14 operation(s) for certificates.
  name: InfraNest Certificates API
  slug: infranest-certificates-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Cloud API from InfraNest — 54 operation(s) for cloud.
  name: InfraNest Cloud API
  slug: infranest-cloud-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Cost API from InfraNest — 2 operation(s) for cost.
  name: InfraNest Cost API
  slug: infranest-cost-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Cost reporting API from InfraNest — 2 operation(s) for cost reporting.
  name: InfraNest Cost reporting API
  slug: infranest-cost-reporting-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Custom fields API from InfraNest — 3 operation(s) for custom fields.
  name: InfraNest Custom fields API
  slug: infranest-custom-fields-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The DNS API from InfraNest — 19 operation(s) for dns.
  name: InfraNest DNS API
  slug: infranest-dns-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Domains API from InfraNest — 26 operation(s) for domains.
  name: InfraNest Domains API
  slug: infranest-domains-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Drop catch page's Overview (#3004) and its Results tab. Every verdict is `DropCatchOverview`'s, read per watch through the same `WatchReading` the watch list draws its rows from; the page words it
  name: InfraNest Drop Catch API
  slug: infranest-drop-catch-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Dynamic IP API from InfraNest — 10 operation(s) for dynamic ip.
  name: InfraNest Dynamic IP API
  slug: infranest-dynamic-ip-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Endpoints API from InfraNest — 105 operation(s) for endpoints.
  name: InfraNest Endpoints API
  slug: infranest-endpoints-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Integration Logs API from InfraNest — 1 operation(s) for integration logs.
  name: InfraNest Integration Logs API
  slug: infranest-integration-logs-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Integrations API from InfraNest — 6 operation(s) for integrations.
  name: InfraNest Integrations API
  slug: infranest-integrations-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Monitoring API from InfraNest — 40 operation(s) for monitoring.
  name: InfraNest Monitoring API
  slug: infranest-monitoring-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: The Organizations API from InfraNest — 4 operation(s) for organizations.
  name: InfraNest Organizations API
  slug: infranest-organizations-api
- baseURL: https://api.infranest.io
  baseurl_source: declared
  description: Outbound webhook endpoints (#30) — org members subscribe an external URL to InfraNest events and receive signed POSTs. The signing secret is returned only on create / rotate.
  name: InfraNest Webhooks API
  slug: infranest-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Infranest Webhooks
  slug: infranest-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/infranest/agentic-access/infranest-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/infranest-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/infranest/plans/infranest-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infranest-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/infranest/rules/infranest-rules.yml
  title: ''
  type: Spectral
  url: rules/infranest-rules.yml
- group: design
  href: https://artifacts.apis.io/infranest/json-ld/infranest-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/infranest-context.jsonld
- group: design
  href: https://artifacts.apis.io/infranest/vocabulary/infranest-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/infranest-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/infranest/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/infranest/asyncapi/infranest-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/infranest-webhooks.yml
- group: design
  href: https://artifacts.apis.io/infranest/data-model/infranest-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infranest-data-model.yml
- group: operate
  href: https://artifacts.apis.io/infranest/changelog/infranest-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/infranest-changelog.yml
- group: design
  href: https://artifacts.apis.io/infranest/conventions/infranest-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/infranest-conventions.yml
- group: design
  href: https://artifacts.apis.io/infranest/conventions/infranest-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infranest-conventions.yml
- group: start
  href: https://artifacts.apis.io/infranest/sandbox/infranest-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/infranest-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://infranest.io/security/
- group: auth
  href: https://artifacts.apis.io/infranest/authentication/infranest-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infranest-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.infranest.io/versioning.md
- group: design
  href: https://artifacts.apis.io/infranest/lifecycle/infranest-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/infranest-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/infranest/errors/infranest-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infranest-problem-types.yml
- group: design
  href: https://artifacts.apis.io/infranest/conformance/infranest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infranest-conformance.yml
- group: agent
  href: https://artifacts.apis.io/infranest/llms/infranest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infranest-llms.txt
- group: auth
  href: https://artifacts.apis.io/infranest/well-known/infranest-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/infranest-security.txt
- group: auth
  href: https://artifacts.apis.io/infranest/well-known/infranest-pages-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/infranest-pages-security.txt
- group: auth
  href: https://artifacts.apis.io/infranest/well-known/infranest-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/infranest-app-security.txt
- group: auth
  href: https://artifacts.apis.io/infranest/well-known/infranest-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/infranest-api-security.txt
- group: agent
  href: https://artifacts.apis.io/infranest/well-known/infranest-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/infranest-well-known.yml
- group: other
  href: https://artifacts.apis.io/infranest/hosts/infranest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infranest-hosts.yml
- group: other
  href: https://artifacts.apis.io/infranest/vendors/infranest-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infranest-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://infranest.io/integrations/webhook/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infranest.io/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infranest.io/
- group: start
  title: ''
  type: SignUp
  url: https://app.infranest.io/register?src=hero&utm_source=infranest.io&utm_medium=referral&utm_campaign=hero
- group: auth
  title: ''
  type: Security
  url: https://infranest.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infranest.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://infranest.io/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InfraNest-Infrastructure-Organized
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.infranest.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://infranest.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.infranest.io/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.infranest.io\
- group: docs
  title: ''
  type: APIReference
  url: https://developers.infranest.io/reference
- group: auth
  href: https://artifacts.apis.io/infranest/security/infranest-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/infranest-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/infranest/security/infranest-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/infranest-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/infranest/security/infranest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infranest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infranest.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.infranest.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://developers.infranest.io/openapi.json
  - status: 401
    url: https://api.infranest.io/mcp
  - status: 200
    url: https://infranest.io
  reason: partner-login
  state: gated
created: '2026-11-03'
description: InfraNest provides a unified dashboard for managing domains, DNS records, SSL certificates, servers and uptime monitoring across multiple providers. Users can connect existing services in minutes without migration, gaining centralized visibility and control over their infrastructure. The platform emphasizes ease of use, security, and comprehensive monitoring for modern cloud environments.
image: https://infranest.io/og.png
jsonld:
- class_count: 1
  name: Infranest Context
  property_count: 10
  slug: infranest-context
layout: provider
modified: '2026-11-03'
name: InfraNest
nav: Providers
network: true
overview: 'InfraNest publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit Log API, Authentication API, Automations API, and 16 more. Tagged areas include Company, Infrastructure, DNS, Monitoring, and SSL.


  The InfraNest catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  InfraNest''s developer surface includes changelog, sandbox, authentication, signup flow, pricing, engineering blog, getting-started guide, and 37 more developer resources.'
plans:
- name: Infranest Plans Pricing
  plan_count: 4
  slug: infranest-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: InfraNest API Rules
  rule_count: 61
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 5
  slug: infranest-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 12.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 65.2
    developer_ergonomics: 41.1
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Infranest Authentication
  slug: infranest-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Infranest Domain Security
  slug: infranest-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Infranest Vulnerability Disclosure
  slug: infranest-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Infranest Trust Center
  slug: infranest-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
skill_count: 4
skills:
- name: infranest-apply-dns-template
  slug: infranest-apply-dns-template
- name: infranest-auth-logout
  slug: infranest-auth-logout
- name: infranest-create-and-run-monitor
  slug: infranest-create-and-run-monitor
- name: infranest-set-manual-price
  slug: infranest-set-manual-price
slug: infranest
tags:
- Company
- Infrastructure
- DNS
- Monitoring
- SSL
- Cloud
website: https://infranest.io
---
