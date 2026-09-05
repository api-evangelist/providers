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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Air Force Reserve Command (AFRC) provides information on reserve programs, career opportunities, unit locations, benefits, and recruiting resources for prospective and current reservists.
  name: Air Force Reserve Command
  slug: afrc
artifact_total: 28
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/air-force-reserve-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airforcereserverecruiting
- group: company
  title: ''
  type: Website
  url: https://www.afrc.af.mil/
- group: start
  title: ''
  type: Portal
  url: https://www.airforce.com/ways-to-serve/air-force-reserve
- group: start
  title: ''
  type: Portal
  url: https://myfss.us.af.mil/
- group: start
  title: ''
  type: Portal
  url: https://www.my.af.mil/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afrc.af.mil/Privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/air-force-reserve-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.airforce.com/frequently-asked-questions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airforce.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airforce.com/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.airforce.com/accessibility
coverage:
  checked: '2026-08-30'
  detail: AFRC is a United States military command whose only public web properties are a public-affairs site and the airforce.com recruiting site; airforce.com was fully crawlable and served a 404 for /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and every /.well-known/ discovery path, and the member systems it links (myFSS, the Air Force Portal) are DoD-credentialed applications, not a developer program.
  evidence:
  - status: 404
    url: https://www.airforce.com/openapi.json
  - status: 404
    url: https://www.airforce.com/.well-known/agent-card.json
  - status: 200
    url: https://www.airforce.com/robots.txt
  - status: 403
    url: https://www.afrc.af.mil/
  - status: 0
    url: https://mypers.af.mil/
  reason: no-developer-program
  state: none
created: '2024-11-21'
description: The Air Force Reserve (AFRC) is the reserve component of the United States Air Force, headquartered at Robins Air Force Base, Georgia. It provides trained units and individuals to be available for active duty in time of war, national emergency, or when otherwise authorized by law. Air Force Reserve members serve part-time, typically one weekend per month and two weeks per year, while maintaining civilian careers. AFRC does not currently provide a public developer API but offers digital recruitment and informational resources.
examples:
- key_count: 6
  name: Afrc Career Opportunity Example
  slug: afrc-career-opportunity-example
- key_count: 8
  name: Afrc Reserve Member Example
  slug: afrc-reserve-member-example
- key_count: 6
  name: Afrc Reserve Unit Example
  slug: afrc-reserve-unit-example
features:
- description: Part-time service obligation of one weekend per month and 14 days per year with full access to Air Force training and benefits.
  name: Traditional Reserve Service
- description: Full-time active-duty positions within the Reserve component with all active-duty benefits.
  name: Active Guard Reserve (AGR)
- description: Reserve positions augmenting active-duty units during contingencies and deployments.
  name: Individual Mobilization Augmentee (IMA)
- description: Dual-status civilian/military positions serving as both federal civil servant and reserve member.
  name: Air Reserve Technician (ART)
- description: Over 200 career specialties available across aviation, intelligence, cyber, medical, maintenance, and many other fields.
  name: 200+ Career Fields
- description: Reserve Educational Assistance Program (REAP), GI Bill benefits, and tuition assistance for qualifying reservists.
  name: Educational Benefits
- description: Transition programs allowing active-duty airmen to transfer to the Reserve component.
  name: Palace Chase/Front Programs
- description: Access to TRICARE Reserve Select healthcare coverage for qualifying Reserve members and families.
  name: Healthcare Benefits
finops:
- name: Air Force Reserve Finops
  service_category: API
  slug: air-force-reserve-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/air-force-reserve.png
json_schemas:
- name: CareerOpportunity
  property_count: 6
  slug: afrc-career-opportunity
- name: ReserveMember
  property_count: 8
  slug: afrc-reserve-member
- name: ReserveUnit
  property_count: 6
  slug: afrc-reserve-unit
json_structures:
- name: Afrc Career Opportunity Structure
  property_count: 6
  slug: afrc-career-opportunity-structure
- name: Afrc Reserve Member Structure
  property_count: 8
  slug: afrc-reserve-member-structure
- name: Afrc Reserve Unit Structure
  property_count: 6
  slug: afrc-reserve-unit-structure
jsonld:
- class_count: 3
  name: Afrc Context
  property_count: 9
  slug: afrc-context
layout: provider
modified: '2026-08-30'
name: Air Force Reserve
nav: Providers
network: true
overview: 'Air Force Reserve publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Military, Defense, Air Force, and United States Government.


  The Air Force Reserve catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Air Force Reserve''s developer surface includes developer portal, support, and 10 more developer resources.'
plans:
- name: Air Force Reserve Plans Pricing
  plan_count: 0
  slug: air-force-reserve-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Air Force Reserve Rate Limits
  slug: air-force-reserve-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Air Force Reserve API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: air-force-reserve-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 43.3
    catalog_earned_first_party: 0.0
    catalog_gap: 71.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 6.7
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 21.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/air-force-reserve/refs/heads/main/screenshots/air-force-reserve-2026-06-20T171412.png
security:
- kind: domain-security
  name: Air Force Reserve Domain Security
  slug: air-force-reserve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: air-force-reserve
tags:
- Federal-Government
- Military
- Defense
- Air Force
- United States Government
use_cases:
- description: Connect prospective members with available Air Force Reserve career opportunities and units.
  name: Reserve Recruiting
- description: Support active-duty airmen transitioning to Reserve status via Palace Chase/Front programs.
  name: Active Duty Transition
- description: Provide trained reserve units and individuals to augment active-duty missions during contingencies.
  name: Unit Deployment Support
- description: Reserve cyber squadrons and intelligence units supporting national security missions part-time.
  name: Cyber and Intelligence Missions
website: https://www.afrc.af.mil/
---
