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
api_count: 1
apis:
- description: The canonical Cloudflare REST API at https://api.cloudflare.com/client/v4 covering account management, DNS and zones, SSL/TLS certificates, WAF and firewall rules, Workers and KV, R2 object storage, P
  name: Cloudflare API (canonical)
  slug: canonical
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudflare-com-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudflare
- group: company
  title: ''
  type: Website
  url: https://www.cloudflare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cloudflare.com/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cloudflarestatus.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudflare.com/privacypolicy/
- group: other
  title: ''
  type: Canonical
  url: https://github.com/api-evangelist/cloudflare
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cloudflare.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/rss/
created: '2024-01-01'
description: cloudflare-com is an alias profile for Cloudflare. The canonical company profile lives at the cloudflare repository in the API Evangelist Network; this entry exists so that the ".com" form of the brand resolves into the same canonical record. Cloudflare's developer surface includes a single unified REST API at api.cloudflare.com covering DNS, zones, SSL/TLS, Workers, KV, Durable Objects, Queues, R2, Pages, Stream, Email Routing, Zero Trust, WAF, Magic Transit, Spectrum, Load Balancing, Analytics, and Account Management. Authentication is via API tokens with scoped permissions or legacy global API keys.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudflare-com.png
layout: provider
modified: '2026-04-25'
name: Cloudflare.com
nav: Providers
network: true
overview: 'Cloudflare.com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Alias, Application Services, CDN, DNS, and Edge Computing.


  Cloudflare.com''s developer surface includes documentation, API reference, engineering blog, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 15.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudflare-com/refs/heads/main/screenshots/cloudflare-com-2026-06-20T174554.png
security:
- kind: domain-security
  name: Cloudflare Com Domain Security
  slug: cloudflare-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare Com Vulnerability Disclosure
  slug: cloudflare-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cloudflare-com
tags:
- Alias
- Application Services
- CDN
- DNS
- Edge Computing
- Email
- Network
- Security
- Workers
- Zero Trust
website: https://www.cloudflare.com/
---
