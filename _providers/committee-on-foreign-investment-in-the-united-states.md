---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius'', ''status'': 302, ''note'': ''declared website redirects to https://www.cfius.gov/ — a different registrable domain (treasury.gov -> cfius.gov), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: CFIUS publishes an annual report to Congress summarizing covered transactions reviewed during the prior calendar year, statistics on notices, declarations, withdrawn cases, and presidential decisions.
  name: CFIUS Annual Report to Congress
  slug: annual-reports
- description: 'CFIUS provides guidance for parties submitting declarations (short-form filings) and joint voluntary notices (full-form filings) for covered transactions. The Treasury maintains forms, FAQs, and case '
  name: CFIUS Declarations and Notices Guidance
  slug: declarations-and-notices
- description: The CFIUS regulatory framework is published in 31 CFR Parts 800, 801, and 802, and is anchored in Section 721 of the Defense Production Act as amended by FIRRMA. Regulations and statutes are available
  name: CFIUS Regulations and Statutes
  slug: regulations
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/committee-on-foreign-investment-in-the-united-states-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius
- group: docs
  title: ''
  type: Documentation
  url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-laws-and-guidance
- group: docs
  title: ''
  type: Reference
  url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII
- group: other
  title: ''
  type: Reports
  url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-reports-and-tables
- group: operate
  title: ''
  type: FAQ
  url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-frequently-asked-questions-faqs
created: '2024-12-03'
description: The Committee on Foreign Investment in the United States (CFIUS) is an inter-agency committee chaired by the U.S. Department of the Treasury that reviews certain foreign investment transactions for national security implications. CFIUS reviews are governed by the Defense Production Act and Section 721, and were significantly strengthened by the Foreign Investment Risk Review Modernization Act of 2018 (FIRRMA). On September 15, 2022, President Biden issued Executive Order 14083 directing CFIUS to focus on emerging national security risks. CFIUS work is largely confidential, and the public-facing surface is limited to regulations, annual reports to Congress, FAQs, declarations and notices guidance, and case studies.
finops:
- name: Committee On Foreign Investment In The United States Finops
  service_category: API
  slug: committee-on-foreign-investment-in-the-united-states-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/committee-on-foreign-investment-in-the-united-states.png
layout: provider
modified: '2026-04-28'
name: Committee on Foreign Investment in the United States
nav: Providers
network: true
overview: 'Committee on Foreign Investment in the United States publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CFIUS, Federal-Government, Foreign Investment, National Security, and Regulations.


  Committee on Foreign Investment in the United States'' developer surface includes documentation, FAQ, and 4 more developer resources.'
plans:
- name: Committee On Foreign Investment In The United States Plans Pricing
  plan_count: 3
  slug: committee-on-foreign-investment-in-the-united-states-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Committee On Foreign Investment In The United States Rate Limits
  slug: committee-on-foreign-investment-in-the-united-states-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/committee-on-foreign-investment-in-the-united-states/refs/heads/main/screenshots/committee-on-foreign-investment-in-the-united-states-2026-06-20T174816.png
security:
- kind: domain-security
  name: Committee On Foreign Investment In The United States Domain Security
  slug: committee-on-foreign-investment-in-the-united-states-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: committee-on-foreign-investment-in-the-united-states
tags:
- CFIUS
- Federal-Government
- Foreign Investment
- National Security
- Regulations
- Treasury
website: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius
---
