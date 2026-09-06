---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://newcore.com
- group: company
  title: ''
  type: Blog
  url: https://newcore.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newcore.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newcore.com/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.newcore.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.newcore.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.newcore.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/newcore-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/newcore-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/newcore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newcore-domain-security.yml
created: '2026-07-17'
description: NewCore is an enterprise identity-security company building an identity platform that governs both human and AI-agent identities across the enterprise. Its three pillars are Identity Discovery (continuously discovering and mapping every identity across directories, PAM, shadow systems, and AI infrastructure), Identity Security (breach prevention through phishing-resistant authentication and device-bound sessions that cannot be stolen or replayed), and Human + AI Agent Governance (minimum-access provisioning, full lifecycle management, and support for ephemeral agentic workloads). NewCore is backed by Index Ventures. It sells to enterprises via demo request and publishes a trust center (SOC 2 Type II, CSA STAR Level 1, GDPR, CCPA) but does not currently expose a public developer API, SDKs, or API documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newcore.png
layout: provider
modified: '2026-07-20'
name: NewCore
nav: Providers
network: true
overview: 'NewCore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity, IAM, and Authentication.


  NewCore''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newcore/refs/heads/main/screenshots/newcore-2026-08-07T185057.png
security:
- kind: domain-security
  name: Newcore Domain Security
  slug: newcore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Newcore Vulnerability Disclosure
  slug: newcore-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Newcore Trust Center
  slug: newcore-trust-center
  summary_line: SOC 2 Type II, CSA STAR Level 1, GDPR, CCPA
slug: newcore
tags:
- Company
- Security
- Identity
- IAM
- Authentication
- AI Agents
- Governance
- Zero Trust
website: https://newcore.com
---
