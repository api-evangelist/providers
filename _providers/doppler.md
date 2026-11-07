---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Doppler Agentic Access
  operation_count: 19
  slug: doppler-agentic-access
  summary_line: 19 operations · 7 acting
api_count: 1
apis:
- description: Versioned REST API (v3) for managing Doppler workplaces, projects, environments, configs, secrets, dynamic secrets, service tokens, service accounts, integrations, audit logs, and webhooks. Authentica
  name: Doppler REST API
  slug: rest-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The Workplace API from Doppler — 2 operation(s) for workplace.
  name: Doppler Workplace API
  slug: doppler-workplace-api
artifact_total: 17
collections:
- collection_type: open
  name: Doppler REST ActivityLogs API
  slug: open-doppler-activitylogs-api
- collection_type: open
  name: Doppler REST ActivityLogs Auth API
  slug: open-doppler-auth-api
- collection_type: open
  name: Doppler REST ActivityLogs Configs API
  slug: open-doppler-configs-api
- collection_type: open
  name: Doppler REST ActivityLogs Environments API
  slug: open-doppler-environments-api
- collection_type: open
  name: Doppler REST ActivityLogs Projects API
  slug: open-doppler-projects-api
- collection_type: open
  name: Doppler REST ActivityLogs Secrets API
  slug: open-doppler-secrets-api
- collection_type: open
  name: Doppler REST ActivityLogs ServiceTokens API
  slug: open-doppler-servicetokens-api
- collection_type: open
  name: Doppler REST ActivityLogs Webhooks API
  slug: open-doppler-webhooks-api
- collection_type: open
  name: Doppler REST API
  slug: open-doppler
common:
- group: other
  href: https://artifacts.apis.io/doppler/capabilities/doppler-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/doppler-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/doppler/agentic-access/doppler-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doppler-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/doppler/security/doppler-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/doppler-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/doppler/security/doppler-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doppler-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/doppler/security/doppler-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doppler-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/doppler/authentication/doppler-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doppler-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dopplerhq
- group: company
  title: ''
  type: Website
  url: https://www.doppler.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.doppler.com
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.doppler.com/reference/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doppler.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.doppler.com/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DopplerHQ
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.doppler.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.doppler.com/blog/rss.xml
created: '2026-05-11'
description: Doppler is a centralized, cloud-based SecretOps platform that manages application configuration and secrets for humans, CI/CD pipelines, and AI agents across environments. It provides Git-style activity logs, rollbacks, webhooks, SDKs, and deep integrations with AWS, Azure, GCP, Kubernetes, and the major CI providers, with SOC 2 and ISO compliance. The Doppler REST API offers full programmatic control over projects, configs, secrets, tokens, service accounts, and audit logs using Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doppler.png
layout: provider
modified: '2026-05-11'
name: Doppler
nav: Providers
network: true
overview: 'Doppler publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Workplace API, and 1 more. Tagged areas include Secrets Management, SecretOps, DevOps, Configuration Management, and Security.


  The Doppler catalog on APIs.io includes 1 Spectral governance ruleset.


  Doppler''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 10 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Doppler API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: doppler-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 47.0
    developer_ergonomics: 42.9
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 10.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/doppler/doppler-2026-06-20T180156.png
security:
- kind: authentication
  name: Doppler Authentication
  slug: doppler-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doppler Domain Security
  slug: doppler-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doppler Vulnerability Disclosure
  slug: doppler-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Doppler Trust Center
  slug: doppler-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: doppler
tags:
- Secrets Management
- SecretOps
- DevOps
- Configuration Management
- Security
- CI/CD
- Developer Tools
website: https://www.doppler.com
---
