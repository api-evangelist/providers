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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/academi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constellis.com/constellis-training-center/
coverage:
  checked: '2026-09-06'
  detail: 'ACADEMI is a retired brand, not a live company - Academi Training Center, LLC was one of seven entities merged into Constellis Holdings in June 2014, and Constellis states on its own site that "Constellis does not operate under the Academi name" - and the domain academi.com is now web-retired: port 443 fails the TLS handshake outright and port 80 returns HTTP 409 with a Cloudflare error-1001 body on every path, while DNS keeps only mail (Proofpoint MX, SPF, DMARC p=reject reporting to itsec@constellis.com).'
  evidence:
  - status: 409
    url: http://academi.com/
  - status: 0
    url: https://academi.com/
  - status: 409
    url: http://academi.com/openapi.json
  - status: 200
    url: https://constellis.com/constellis-training-center/
  - status: 404
    url: https://constellis.com/.well-known/api-catalog
  reason: defunct
  state: none
created: '2026-09-06'
description: 'ACADEMI was the 2011-2014 name of the American private military, security and training company founded on 26 December 1996 in North Carolina by Erik Prince and Al Clark as Blackwater. It was renamed Blackwater Worldwide in October 2007 after the Nisour Square shooting in Baghdad, then Xe Services LLC in February 2009. In December 2010 the training business and its Moyock, North Carolina campus - the largest private training facility in the United States - were bought by USTC Holdings, an investor consortium led by Forte Capital Advisors and Manhattan Strategic Ventures, ending Erik Prince''s involvement, and the company was rebranded ACADEMI in December 2011 under chairman Red McCombs. In June 2014 Academi Training Center, LLC was merged with Triple Canopy, Constellis Ltd., Strategic Social, Tidewater Global Services, National Strategic Protective Services and International Development Solutions to form Constellis Holdings, which Apollo Global Management acquired in September
  2016 and which is headquartered in Herndon, Virginia. The ACADEMI brand was retired in the merger: Constellis states on its own site that "Academi remains part of historical, legal, and contractual records, but Constellis does not operate under the Academi name", and the Moyock campus now trades as the Constellis Training Center. The business sells physical services - firearms, driving, maritime, K-9, UAS/C-UAS and advanced security and military training, protective security details, and logistics and complex program management for United States government customers - not software. It never operated a developer program, public API, SDK, webhook surface or machine-readable API specification, and academi.com no longer serves a website: the domain is retained by Constellis for email only. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-06'
name: Academi
nav: Providers
network: true
overview: Academi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defense, Private Military, Security Services, and Physical Security.
random_paper: 15
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  previous_composite: 3.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Academi Domain Security
  slug: academi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: academi
tags:
- Company
- Defense
- Private Military
- Security Services
- Physical Security
- Training
- Government Contracting
- Logistics
- Program Management
- Acquired
- Brand Retired
website: https://constellis.com/constellis-training-center/
---
