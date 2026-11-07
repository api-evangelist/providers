---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Advanceai Agentic Access
  operation_count: 9
  slug: advanceai-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.advance.ai
  baseurl_source: declared
  description: Exchange an access key and request signature for a short-lived access token.
  name: ADVANCE.AI Authentication API
  slug: advanceai-authentication-api
- baseURL: https://api.advance.ai
  baseurl_source: declared
  description: Global Document Verification — SDK licensing and result query with OCR and forgery detection.
  name: ADVANCE.AI Document Verification API
  slug: advanceai-document-verification-api
- baseURL: https://api.advance.ai
  baseurl_source: declared
  description: Compare two face photographs and return a similarity score.
  name: ADVANCE.AI Face Comparison API
  slug: advanceai-face-comparison-api
- baseURL: https://api.advance.ai
  baseurl_source: declared
  description: Liveness session licensing, result retrieval, video evidence and PII data retention.
  name: ADVANCE.AI Liveness Detection API
  slug: advanceai-liveness-detection-api
artifact_total: 16
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://advance.ai/feed/
- group: agent
  href: https://artifacts.apis.io/advanceai/agentic-access/advanceai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/advanceai-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://advance.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.advance.ai/global_document_verification.html
- group: docs
  title: ''
  type: APIReference
  url: https://doc.advance.ai/liveness_detection.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.advance.ai/
- group: operate
  title: ''
  type: Support
  url: https://support.advance.ai/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://advance.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advance.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advance.ai/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://advance.ai/book-free-demo/
- group: auth
  title: ''
  type: Compliance
  url: https://advance.ai/security-compliance/
- group: auth
  href: https://artifacts.apis.io/advanceai/security/advanceai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/advanceai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/advanceai/security/advanceai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/advanceai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/advanceai/security/advanceai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/advanceai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/advanceai/security/advanceai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/advanceai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/advanceai/authentication/advanceai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/advanceai-authentication.yml
- group: design
  href: https://artifacts.apis.io/advanceai/conventions/advanceai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/advanceai-conventions.yml
- group: design
  href: https://artifacts.apis.io/advanceai/conformance/advanceai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/advanceai-conformance.yml
- group: design
  href: https://artifacts.apis.io/advanceai/errors/advanceai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/advanceai-error-codes.yml
- group: design
  href: https://artifacts.apis.io/advanceai/lifecycle/advanceai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/advanceai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/advanceai/lifecycle/advanceai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/advanceai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/advanceai/rate-limits/advanceai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/advanceai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/advanceai/plans/advanceai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/advanceai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/advanceai/packages/advanceai-packages.yml
  title: ''
  type: Packages
  url: packages/advanceai-packages.yml
- group: build
  href: https://artifacts.apis.io/advanceai/packages/advanceai-packages.yml
  title: ''
  type: SDKs
  url: packages/advanceai-packages.yml
- group: design
  href: https://artifacts.apis.io/advanceai/data-model/advanceai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/advanceai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/advanceai/mcp/advanceai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/advanceai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/advanceai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/advanceai/llms/advanceai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/advanceai-llms.txt
- group: other
  href: https://artifacts.apis.io/advanceai/overlays/advanceai-open-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/advanceai-open-api-overlay.yaml
created: '2026-09-07'
description: 'ADVANCE.AI is the digital identity verification, KYC/KYB, AML, compliance and risk-management business unit of Advance Intelligence Group, headquartered in Singapore and founded in 2016. Its AdvanGuard product line covers identity verification, document verification, face authentication and Know Your Business checks for banking and financial services, fintech, crypto, payments, e-commerce and the sharing economy, with a strong footprint across Southeast Asia and other emerging markets. ADVANCE.AI publishes a public Open API at api.advance.ai documented at doc.advance.ai — token authentication, Global Document Verification with OCR field extraction and ID forgery detection, face comparison, and liveness detection with video evidence and PII data retention — plus first-party Android and iOS capture SDKs distributed from its own Maven and object-storage endpoints. Onboarding is sales-led: there is no self-service sign-up and no published pricing, and platform access keys are issued
  through the Websaas platform.'
image: https://advance.ai/wp-content/uploads/2025/09/top-header-right-image.webp
layout: provider
modified: '2026-10-06'
name: ADVANCE.AI
nav: Providers
network: true
overview: 'ADVANCE.AI publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Document Verification API, Face Comparison API, and 1 more. Tagged areas include Company, Identity Verification, KYC, KYB, and AML.


  The ADVANCE.AI catalog on APIs.io includes 1 Spectral governance ruleset.


  ADVANCE.AI''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Advanceai Plans Pricing
  plan_count: 0
  slug: advanceai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Advanceai Rate Limits
  slug: advanceai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: ADVANCE.AI API Rules
  rule_count: 64
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 1
  slug: advanceai-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 14.3
    developer_ergonomics: 44.6
    discoverability: 66.1
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 31.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/advanceai/advanceai-2026-10-11T092842.png
security:
- kind: authentication
  name: Advanceai Authentication
  slug: advanceai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Advanceai Domain Security
  slug: advanceai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Advanceai Vulnerability Disclosure
  slug: advanceai-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Advanceai Trust Center
  slug: advanceai-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: advanceai-authenticate
  slug: advanceai-authenticate
- name: advanceai-document-verification
  slug: advanceai-document-verification
- name: advanceai-face-comparison
  slug: advanceai-face-comparison
- name: advanceai-liveness-detection
  slug: advanceai-liveness-detection
slug: advanceai
tags:
- Company
- Identity Verification
- KYC
- KYB
- AML
- Fraud Prevention
- Face Recognition
- Liveness Detection
- OCR
- Document Verification
- Risk Management
- Artificial Intelligence
- Fintech
- Singapore
website: https://advance.ai/
---
