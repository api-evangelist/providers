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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
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
  description: The ActivityLogs API from Doppler — 1 operation(s) for activitylogs.
  name: Doppler ActivityLogs API
  slug: doppler-activitylogs-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The Auth API from Doppler — 1 operation(s) for auth.
  name: Doppler Auth API
  slug: doppler-auth-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The Configs API from Doppler — 2 operation(s) for configs.
  name: Doppler Configs API
  slug: doppler-configs-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The Environments API from Doppler — 1 operation(s) for environments.
  name: Doppler Environments API
  slug: doppler-environments-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The Projects API from Doppler — 2 operation(s) for projects.
  name: Doppler Projects API
  slug: doppler-projects-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The Secrets API from Doppler — 3 operation(s) for secrets.
  name: Doppler Secrets API
  slug: doppler-secrets-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The ServiceTokens API from Doppler — 1 operation(s) for servicetokens.
  name: Doppler ServiceTokens API
  slug: doppler-servicetokens-api
- baseURL: https://api.doppler.com/v3
  baseurl_source: declared
  description: The Webhooks API from Doppler — 1 operation(s) for webhooks.
  name: Doppler Webhooks API
  slug: doppler-webhooks-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doppler-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/doppler-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doppler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doppler-domain-security.yml
- group: auth
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
overview: 'Doppler publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ActivityLogs API, Auth API, Configs API, and 5 more. Tagged areas include Secrets Management, SecretOps, DevOps, Configuration Management, and Security.


  Doppler''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doppler/refs/heads/main/screenshots/doppler-2026-06-20T180156.png
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
website: https://www.doppler.com
---
