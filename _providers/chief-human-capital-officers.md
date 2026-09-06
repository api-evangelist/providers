---
access_model:
  confidence: high
  label: Free and unauthenticated
  onboarding: unknown
  pricing: free
  public: true
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
- description: The CHCO Council publishes its charter, leadership roster, working group output, policy memoranda, and federal human capital guidance through chcoc.gov (now hosted under opm.gov). The Council does not
  name: Chief Human Capital Officers Council Resources
  slug: chcoc-resources
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chief-human-capital-officers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opm.gov/chcoc
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.chcoc.gov/
- group: other
  title: ''
  type: ParentAgency
  url: https://www.opm.gov
- group: other
  title: ''
  type: Statute
  url: https://www.law.cornell.edu/uscode/text/5/1401
- group: company
  title: ''
  type: USAJobs
  url: https://www.usajobs.gov/
- group: other
  title: ''
  type: PerformanceManagement
  url: https://www.opm.gov/policy-data-oversight/performance-management/
- group: other
  title: ''
  type: USAGov
  url: https://www.usa.gov/agencies/chief-human-capital-officers-council
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opm.gov/privacy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chief-human-capital-officers-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.opm.gov/vulnerability-disclosure-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chief-human-capital-officers-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/chief-human-capital-officers-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chief-human-capital-officers-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://www.opm.gov/about-us/contact-us/
- group: other
  title: ''
  type: WorkingGroups
  url: ''
- group: other
  title: ''
  type: Standards
  url: ''
coverage:
  checked: '2026-09-05'
  detail: The CHCO Council is a statutory interagency policy forum (5 U.S.C. 1401-1402), not a software producer — it publishes HR policy memos, annual reports and a member roster as web pages and PDFs, its own chcoc.gov domain 301s wholesale into https://www.opm.gov/chcoc, and full STEP 0b contract discovery across chcoc.gov, www.chcoc.gov, beta.chcoc.gov, opm.gov, www.opm.gov and data.opm.gov turned up no OpenAPI, GraphQL, MCP, agent card or /.well-known/ document of any kind.
  evidence:
  - status: 200
    url: https://www.opm.gov/chcoc
  - status: 404
    url: https://www.opm.gov/openapi.json
  - status: 404
    url: https://www.opm.gov/.well-known/api-catalog
  - status: 301
    url: https://www.chcoc.gov/openapi.json
  - status: 200
    url: https://beta.chcoc.gov/openapi.json
  - status: 0
    url: https://hru.gov/
  reason: not-a-software-company
  state: none
created: '2024-12-03'
description: The Chief Human Capital Officers (CHCO) Council is the principal interagency forum to advise and coordinate the activities of members on matters of modernization of human resources (HR) systems, improved quality of human resources information, and legislation affecting human resources operations and organizations across the U.S. federal government. Established under the Chief Human Capital Officers Act of 2002 (5 U.S.C. 1401-1402), the Council is chaired by the Director of the U.S. Office of Personnel Management (OPM) with the Deputy Director for Management at OMB serving as Vice Chair. The CHCO Council coordinates federal human capital management strategy, supports the Federal HR workforce, advances workforce planning and talent acquisition, and oversees performance management, employee engagement, learning and development, and HR policy implementation across departments and agencies.
features:
- name: Senior-Level Interagency Forum
- name: Federal Human Capital Policy Coordination
- name: HR Workforce Capacity Building
- name: Human Capital Strategic Planning
- name: Talent Acquisition and Hiring Reform
- name: Performance Management Guidance
- name: Employee Engagement Surveys (FEVS)
- name: Learning and Development Standards
finops:
- name: Chief Human Capital Officers Finops
  service_category: API
  slug: chief-human-capital-officers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chief-human-capital-officers.png
layout: provider
modified: '2026-09-05'
name: Chief Human Capital Officers Council
nav: Providers
network: true
overview: 'Chief Human Capital Officers Council publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CHCO, Federal-Government, HR Policy, Human Capital, and Human Resources.


  Chief Human Capital Officers Council''s developer surface includes support and 14 more developer resources.'
plans:
- name: Chief Human Capital Officers Plans Pricing
  plan_count: 0
  slug: chief-human-capital-officers-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Chief Human Capital Officers Rate Limits
  slug: chief-human-capital-officers-rate-limits
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chief-human-capital-officers/refs/heads/main/screenshots/chief-human-capital-officers-2026-06-20T174308.png
security:
- kind: domain-security
  name: Chief Human Capital Officers Domain Security
  slug: chief-human-capital-officers-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chief Human Capital Officers Vulnerability Disclosure
  slug: chief-human-capital-officers-vulnerability-disclosure
  summary_line: Bugcrowd
slug: chief-human-capital-officers
tags:
- CHCO
- Federal-Government
- HR Policy
- Human Capital
- Human Resources
- Interagency Council
- OPM
- Public Sector
- Talent Acquisition
- Workforce Management
use_cases:
- name: Federal Hiring Reform
- name: Workforce Planning and Analytics
- name: HR Modernization and Shared Services
- name: Federal Employee Engagement Improvement
- name: Cross-Agency HR Best Practice Sharing
- name: Human Capital Operating Plan Development
- name: HR Workforce Skills Development
website: https://www.opm.gov/chcoc
---
