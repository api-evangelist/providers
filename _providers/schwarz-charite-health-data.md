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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://schwarz-digits.de/
- group: design
  title: ''
  type: Conformance
  url: conformance/schwarz-charite-health-data-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schwarz-charite-health-data-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/schwarz-charite-health-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/schwarz-charite-health-data-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/schwarz-charite-health-data-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Schwarz Charite Health Data GmbH is a March-2026 joint venture that has not yet stood up any web presence of its own - schwarz-charite-health-data.de does not resolve, no company domain was found, and the HIVEPRO product page that used to sit at highmed.org/en/hivepro now 404s, leaving a press release on the parent's site and an openEHR industry-partner card as the company's entire public surface, with no developer portal, documentation or contract anywhere behind them.
  evidence:
  - status: 404
    url: https://www.highmed.org/en/hivepro
  - status: 404
    url: https://schwarz-digits.de/llms.txt
  - status: 404
    url: https://schwarz-digits.de/.well-known/api-catalog
  - status: 200
    url: https://openehr.org/industry-partners/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Schwarz Charite Health Data GmbH is a German health-data joint venture announced on 2026-03-20 by Charite - Universitaetsmedizin Berlin and Schwarz Digits, the IT and digital arm of the Schwarz Group (Lidl, Kaufland, STACKIT). Schwarz Digits holds 75 percent and Charite 25 percent. The venture takes the HIVEPRO platform to market: a clinical data platform whose core is an openEHR-based Clinical Data Repository queried with Archetype Query Language (AQL), able to exchange data over HL7 FHIR - including the German Medical Informatics Initiative (MII) core dataset - and to feed OMOP-compliant analytics. HIVEPRO harmonises and networks records that are otherwise trapped in incompatible hospital source systems, and is delivered as a managed cloud service running on STACKIT''s sovereign cloud so that data residency and control stay in Germany under European data-protection rules. The technical lineage comes from the BMBF-funded HiGHmed consortium, active since 2016. openEHR International
  lists the company as an industry partner. As of this pass the company has no website, developer portal, documentation host or public API of its own; every public surface it has is a press page on its parent''s site.'
image: https://schwarz-cms.object.storage.eu01.onstackit.cloud/schwarz/images/_aliases/16_9_md_8_def/0/9/1/2/1572190-1-ger-DE/39df572a37c9-Charite-und-Schwarz-Digits-gruenden-Joint-Venture_2540x1429px.jpg
layout: provider
modified: '2026-09-02'
name: Schwarz Charite Health Data
nav: Providers
network: true
overview: Schwarz Charite Health Data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Data, Healthcare, Clinical Data Repository, and openEHR.
plans:
- name: Schwarz Charite Health Data Plans Pricing
  plan_count: 0
  slug: schwarz-charite-health-data-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Schwarz Charite Health Data Rate Limits
  slug: schwarz-charite-health-data-rate-limits
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 6.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Schwarz Charite Health Data Domain Security
  slug: schwarz-charite-health-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: schwarz-charite-health-data
tags:
- Company
- Health Data
- Healthcare
- Clinical Data Repository
- openEHR
- Interoperability
- HL7 FHIR
- Data Sovereignty
- Cloud
- Germany
- Joint Venture
website: https://schwarz-digits.de/
---
