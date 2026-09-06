---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.attivonetworks.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.sentinelone.com/platform/identity/ — a different registrable domain (attivonetworks.com -> sentinelone.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: https://www.attivonetworks.com/
- group: other
  title: ''
  type: Product
  url: https://www.sentinelone.com/platform/identity/
- group: company
  title: ''
  type: Blog
  url: https://www.sentinelone.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.sentinelone.com/support/
- group: operate
  title: ''
  type: Community
  url: https://community.sentinelone.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sentinelone.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sentinelone.com/legal/terms-of-service/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/attivo-networks-sentinelone-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/attivo-networks-sentinelone-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/attivo-networks-sentinelone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sentinelone.com/bug-bounty/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sentinelone.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sentinelone.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attivo-networks-sentinelone-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/attivo-networks-sentinelone-llms.txt
created: '2026-07-17'
description: 'Attivo Networks was a pioneer in identity threat detection and response (ITDR), cyber deception, and Active Directory attack protection. SentinelOne acquired Attivo Networks in 2022 and folded its technology into SentinelOne Singularity Identity, part of the AI-powered Singularity security platform spanning endpoint (EDR/XDR), identity, and cloud security. There is no standalone public Attivo API; programmatic access is delivered through the SentinelOne management console REST API (v2.1), which is scoped to a customer''s console URL rather than a public developer portal. This API Evangelist profile tracks the combined entity''s public security, trust, disclosure, and compliance surface: a published RFC 9116 security.txt, a HackerOne-hosted bug bounty, and a SafeBase trust center carrying SOC 2 Type 2, ISO 27001/27017/27018, FedRAMP, and TX-RAMP certifications.'
image: https://www.sentinelone.com/wp-content/uploads/2020/07/sentinelone-logo.png
layout: provider
modified: '2026-07-18'
name: Attivo Networks (SentinelOne)
nav: Providers
network: true
overview: 'Attivo Networks (SentinelOne) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Identity, and ITDR.


  Attivo Networks (SentinelOne)''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/attivo-networks-sentinelone/refs/heads/main/screenshots/attivo-networks-sentinelone-2026-07-25T201722.png
security:
- kind: domain-security
  name: Attivo Networks Sentinelone Domain Security
  slug: attivo-networks-sentinelone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Attivo Networks Sentinelone Vulnerability Disclosure
  slug: attivo-networks-sentinelone-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Attivo Networks Sentinelone Trust Center
  slug: attivo-networks-sentinelone-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27001 SoA, ISO/IEC 27017:2015, ISO/IEC 27018:2019, FedRAMP Certified (Class D), FISMA High, TX-RAMP, Common Criteria, Cyber Essentials, Cyber Essentials Plus, GDPR, CCPA, ACN, VPAT
slug: attivo-networks-sentinelone
tags:
- Company
- Security
- Cybersecurity
- Identity
- ITDR
- Endpoint Security
- Deception
- XDR
website: https://www.attivonetworks.com/
---
