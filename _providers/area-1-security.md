---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.area1security.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.cloudflare.com/sase/products/email-security/ — a different registrable domain (area1security.com -> cloudflare.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/area-1-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.area1security.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/cloudflare-one/email-security/
created: '2026-07-17'
description: Area 1 Security was a cloud-native email security company that built preemptive anti-phishing and business-email-compromise (BEC) protection, discovering and blocking phishing campaigns before they reached inboxes. It could be deployed inline (MX/journaling) or via API connectors to Microsoft 365 and Google Workspace. Cloudflare acquired Area 1 Security in February 2022 for approximately $162 million and folded the technology into its Zero Trust / Cloudflare One platform, where it is now sold as Cloudflare Email Security. The independent area1security.com developer surface has been retired and now redirects to Cloudflare; the product API and documentation live under the Cloudflare developer platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/area-1-security.png
layout: provider
modified: '2026-07-18'
name: Area 1 Security
nav: Providers
network: true
overview: 'Area 1 Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Email Security, Anti-Phishing, and Business Email Compromise.


  Area 1 Security''s developer surface includes documentation and 2 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/area-1-security/refs/heads/main/screenshots/area-1-security-2026-07-25T201116.png
security:
- kind: domain-security
  name: Area 1 Security Domain Security
  slug: area-1-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: area-1-security
tags:
- Company
- Security
- Email Security
- Anti-Phishing
- Business Email Compromise
- Zero Trust
- Cybersecurity
- Cloudflare
- Acquired
website: https://www.area1security.com
---
