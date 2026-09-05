---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.threattracksecurity.com'', ''status'': 301, ''note'': ''declared website redirects to https://vipre.com/ — a different registrable domain (threattracksecurity.com -> vipre.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/threattrack-security-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/threattrack-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/threattrack-security-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://vipre.com/newsroom/responsible-disclosure-win-win/
- group: auth
  title: ''
  type: Compliance
  url: https://vipre.com/about-vipre/compliance-and-certifications/
- group: company
  title: ''
  type: Website
  url: https://www.threattracksecurity.com
created: '2026-07-17'
description: ThreatTrack Security was a cybersecurity vendor focused on advanced malware analysis and threat intelligence, known for its ThreatAnalyzer dynamic malware sandbox, the ThreatIQ real-time threat intelligence feeds, and the VIPRE endpoint antivirus product line. The company traces to Sunbelt Software (founded 1994), which GFI Software acquired in 2010; GFI spun the security unit out in 2013 to form ThreatTrack Security. ThreatTrack was acquired by Ziff Davis / J2 Global in early 2018 and the brand was folded into VIPRE Security Group, so ThreatTrack no longer operates as an independent company. Its historical developer surface was an OEM/on-premise integration API for ThreatAnalyzer (JSON/XML output) and ThreatIQ intelligence feeds rather than a public, self-service developer platform. It was surfaced as a portfolio company of Bessemer Venture Partners and added to the API Evangelist network for enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/threattrack-security.png
layout: provider
modified: '2026-07-21'
name: ThreatTrack Security
nav: Providers
network: true
overview: ThreatTrack Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Threat Intelligence, Malware Analysis, and Sandboxing.
random_paper: 14
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/threattrack-security/refs/heads/main/screenshots/threattrack-security-2026-09-02T163613.png
security:
- kind: domain-security
  name: Threattrack Security Domain Security
  slug: threattrack-security-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Threattrack Security Vulnerability Disclosure
  slug: threattrack-security-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Threattrack Security Trust Center
  slug: threattrack-security-trust-center
  summary_line: SOC 2, HIPAA
slug: threattrack-security
tags:
- Company
- Cybersecurity
- Threat Intelligence
- Malware Analysis
- Sandboxing
- Endpoint Security
- Antivirus
website: https://www.threattracksecurity.com
---
