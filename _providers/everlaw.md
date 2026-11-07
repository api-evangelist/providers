---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The Everlaw REST API provides programmatic access to the Everlaw eDiscovery platform, enabling automation of case management, document uploads, billing reporting, and analytics. API keys are required '
  name: Everlaw REST API
  slug: everlaw-rest-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/everlaw/security/everlaw-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/everlaw-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/everlaw/security/everlaw-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/everlaw-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/everlaw/security/everlaw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/everlaw-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/everlaw/refs/heads/main/plans/everlaw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/everlaw/refs/heads/main/rate-limits/everlaw-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/everlaw/refs/heads/main/finops/everlaw-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.everlaw.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://support.everlaw.com/hc/en-us
- group: operate
  title: ''
  type: Status
  url: https://status.everlaw.com
- group: company
  title: ''
  type: Blog
  url: https://www.everlaw.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.everlaw.com
- group: company
  title: ''
  type: Website
  url: https://www.everlaw.com
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://www.everlaw.com/blog/ai-and-law/everlaw-microsoft-copilot-mcp-integration/
created: '2026-06-13'
description: Everlaw is a cloud-based litigation and eDiscovery platform offering a REST API for managing cases, uploading evidence, running predictive coding, and collaborating on document review. The API enables custom programs to interface directly with Everlaw to automate processes such as custom reporting, billing tracking, and uploading native data. Authentication is via API keys managed by Organization Admins. The platform supports US, UK, EU, Canada, and Australia regional deployments. Everlaw also provides an MCP Server for integration with AI tools such as Claude.
finops:
- has_sources: false
  method: generated
  name: Everlaw Finops
  primary_unit: ''
  service_category: ''
  slug: everlaw-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/everlaw.png
jsonld:
- class_count: 12
  name: Everlaw Context
  property_count: 14
  slug: everlaw-context
layout: provider
modified: '2026-09-13'
name: Everlaw
nav: Providers
network: true
overview: 'Everlaw is listed with 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include eDiscovery, Litigation, Legal Tech, Document Review, and Predictive Coding.


  The Everlaw catalog on APIs.io includes 1 JSON-LD context.


  Everlaw''s developer surface includes documentation, support, status page, engineering blog, and 9 more developer resources.'
plans:
- name: Everlaw Plans Pricing
  plan_count: 2
  slug: everlaw-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Everlaw Rate Limits
  slug: everlaw-rate-limits
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 38.7
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 26.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/everlaw/everlaw-2026-06-20T180906.png
security:
- kind: domain-security
  name: Everlaw Domain Security
  slug: everlaw-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Everlaw Vulnerability Disclosure
  slug: everlaw-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Everlaw Trust Center
  slug: everlaw-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: everlaw
tags:
- eDiscovery
- Litigation
- Legal Tech
- Document Review
- Predictive Coding
- Artificial Intelligence
- Legal
website: https://www.everlaw.com
---
