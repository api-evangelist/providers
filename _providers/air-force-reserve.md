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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
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
  url: https://mypers.af.mil/
- group: start
  title: ''
  type: Portal
  url: https://www.my.af.mil/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afrc.af.mil/Privacy/
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
modified: '2026-04-19'
name: Air Force Reserve
nav: Providers
network: true
overview: 'Air Force Reserve publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Military, Defense, Air Force, and United States Government.


  The Air Force Reserve catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Air Force Reserve''s developer surface includes developer portal and 6 more developer resources.'
plans:
- name: Air Force Reserve Plans Pricing
  plan_count: 3
  slug: air-force-reserve-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Air Force Reserve Rate Limits
  slug: air-force-reserve-rate-limits
rules:
- name: Air Force Reserve API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: air-force-reserve-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.8
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 35.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/air-force-reserve/refs/heads/main/screenshots/air-force-reserve-2026-06-20T171412.png
security:
- kind: domain-security
  name: Air Force Reserve Domain Security
  slug: air-force-reserve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: air-force-reserve
tags:
- Federal Government
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
