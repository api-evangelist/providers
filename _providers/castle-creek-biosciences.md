---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castle-creek-biosciences/refs/heads/main/well-known/castle-creek-biosciences-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/castle-creek-biosciences-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/castle-creek-biosciences/refs/heads/main/well-known/castle-creek-biosciences-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/castle-creek-biosciences-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castle-creek-biosciences/refs/heads/main/hosts/castle-creek-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/castle-creek-biosciences-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castle-creek-biosciences/refs/heads/main/vendors/castle-creek-biosciences-vendors.yml
  title: ''
  type: Vendors
  url: vendors/castle-creek-biosciences-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://castlecreekbio.com/about/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castle-creek-biosciences/refs/heads/main/security/castle-creek-biosciences-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/castle-creek-biosciences-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castle-creek-biosciences/refs/heads/main/security/castle-creek-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/castle-creek-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://castlecreekbio.com
- group: docs
  title: ''
  type: Documentation
  url: https://castlecreekbio.com/technology/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://castlecreekbio.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://castlecreekbio.com/terms-of-use
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://castlecreekbio.com
  - status: 200
    url: https://www.hiive.com/securities/castle-creek-biosciences-stock
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Castle Creek Biosciences is a late‑stage biotechnology company developing autologous fibroblast‑based gene therapies for rare genetic skin disorders such as dystrophic epidermolysis bullosa. The firm conducts a registrational trial of its lead candidate D‑Fi and aims to create transformative, personalized treatments for patients with severe genetic diseases. It operates from Exton, Pennsylvania, and focuses on both ex vivo and in vivo approaches to deliver durable therapeutic outcomes.
image: http://castlecreekbio.com/wp-content/uploads/2020/03/CCB-Logo-500x500-1.png
layout: provider
modified: '2026-10-07'
name: Castle Creek Biosciences
nav: Providers
network: true
overview: 'Castle Creek Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Gene Therapy, Regenerative Medicine, Healthcare, and Biotech Company.


  Castle Creek Biosciences'' developer surface includes documentation and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Castle Creek Biosciences Domain Security
  slug: castle-creek-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Castle Creek Biosciences Vulnerability Disclosure
  slug: castle-creek-biosciences-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: castle-creek-biosciences
tags:
- Biotechnology
- Gene Therapy
- Regenerative Medicine
- Healthcare
- Biotech Company
website: https://castlecreekbio.com
---
