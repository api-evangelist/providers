---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: 'The CAOC publishes its charter, membership roster, meeting summaries, working group output, and federal acquisition guidance through Acquisition.gov. The Council does not expose a dedicated developer '
  name: Chief Acquisition Officers Council Resources
  slug: caoc-resources
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chief-acquisition-officers-council-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chief-acquisition-officers-council-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.acquisition.gov
- group: other
  title: ''
  type: Home
  url: https://www.acquisition.gov/cao-home
- group: other
  title: ''
  type: Charter
  url: https://www.acquisition.gov/caoc-charter
- group: other
  title: ''
  type: PolicyNetwork
  url: https://www.acquisition.gov/policy-network
- group: other
  title: ''
  type: AcquisitionGov
  url: https://www.acquisition.gov
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.whitehouse.gov/omb/
- group: other
  title: ''
  type: USAGov
  url: https://www.usa.gov/agencies/chief-acquisition-officers-council
- group: other
  title: ''
  type: GSAOfficeOfAcquisitionPolicy
  url: https://www.gsa.gov/policy-regulations/policy/acquisition-policy/office-of-acquisition-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acquisition.gov/Privacy_Security
- group: other
  title: ''
  type: WorkingGroups
  url: ''
- group: other
  title: ''
  type: Standards
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.acquisition.gov/rss.xml
coverage:
  checked: '2026-09-05'
  detail: The Council is a statutory interagency forum, not a software publisher — it ships no product, operates no host of its own, and publishes through GSA's Acquisition.GOV, where its own CAOC pages now answer HTTP 403 to anonymous fetches and are absent from the site sitemap while every contract-discovery path on the host returns 404.
  evidence:
  - status: 403
    url: https://www.acquisition.gov/cao-home
  - status: 404
    url: https://www.acquisition.gov/openapi.json
  - status: 404
    url: https://www.acquisition.gov/.well-known/api-catalog
  - status: 404
    url: https://www.acquisition.gov/developers
  reason: not-a-software-company
  state: none
created: '2024-12-03'
description: The Chief Acquisition Officers Council (CAOC) is a senior interagency forum established pursuant to Section 16 of the Office of Federal Procurement Policy Act (41 USC 1311). The Council brings together the Chief Acquisition Officers (CAOs), the Under Secretary of Defense for Acquisition and Sustainment, and the Senior Procurement Executives of Executive Branch agencies to monitor and improve the federal acquisition system, promote effective business practices, deliver best-value products and services, and further integrity, fairness, competition, and openness in federal procurement. The CAOC publishes resources, charters, working group output, and guidance through Acquisition.gov, and operates alongside the Federal Acquisition Regulatory Council and the Office of Management and Budget's Office of Federal Procurement Policy (OFPP).
features:
- name: Senior-Level Interagency Forum
- name: Federal Acquisition Policy Coordination
- name: Working Groups and Action Teams
- name: Acquisition Workforce Development
- name: Best Practice Guidance
- name: Industry Engagement
- name: Performance Reporting
finops:
- name: Chief Acquisition Officers Council Finops
  service_category: API
  slug: chief-acquisition-officers-council-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chief-acquisition-officers-council.png
layout: provider
modified: '2026-09-05'
name: Chief Acquisition Officers Council
nav: Providers
network: true
overview: 'Chief Acquisition Officers Council publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Acquisition, CAOC, FAR, Federal-Government, and GSA.


  Chief Acquisition Officers Council''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Chief Acquisition Officers Council Plans Pricing
  plan_count: 0
  slug: chief-acquisition-officers-council-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Chief Acquisition Officers Council Rate Limits
  slug: chief-acquisition-officers-council-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chief-acquisition-officers-council/refs/heads/main/screenshots/chief-acquisition-officers-council-2026-06-20T174313.png
security:
- kind: domain-security
  name: Chief Acquisition Officers Council Domain Security
  slug: chief-acquisition-officers-council-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chief-acquisition-officers-council
tags:
- Acquisition
- CAOC
- FAR
- Federal-Government
- GSA
- Interagency Council
- OFPP
- OMB
- Procurement
- Public Sector
use_cases:
- name: Federal Acquisition Workforce Improvement
- name: Category Management Adoption
- name: Innovative Buying Practices
- name: Federal Procurement Reporting
- name: Cross-Agency Best Practice Sharing
- name: Industry-Government Collaboration
website: https://www.acquisition.gov
---
