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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The Army National Guard Recruiting API provides access to job listings, Military Occupational Specialties (MOS), unit locations, and recruiter contact information for prospective members interested in
  name: Army National Guard Recruiting API
  slug: recruiting-api
- description: 'The Freedom of Information Act (FOIA) portal for the Army National Guard and National Guard Bureau provides a mechanism for submitting FOIA requests, tracking request status, and accessing previously '
  name: Army National Guard FOIA Portal
  slug: foia-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/army-national-guard-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/army-national-guard
- group: start
  title: Army National Guard Website
  type: Portal
  url: https://www.nationalguard.mil/
- group: docs
  title: Resources
  type: Documentation
  url: https://www.nationalguard.mil/Resources/
- group: build
  title: Army Guard GitHub Organization
  type: GitHubOrganization
  url: https://github.com/armyguard
- group: commercial
  title: Web Policy and Terms
  type: TermsOfService
  url: https://www.nationalguard.mil/About/Web-Policy/
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://www.nationalguard.mil/About/Web-Policy/
created: '2024-12-03'
description: The Army National Guard is a reserve component of the United States Army that serves both the nation and individual states in times of need. Operating under the dual authority of the federal government and the fifty state governors, the Army National Guard provides trained and ready soldiers for overseas military operations, domestic disaster relief, homeland security, and civil support missions. Its primary data and digital services are focused on recruiting, career management, benefits administration, and public outreach. The National Guard Bureau (NGB) coordinates federal operations and maintains administrative systems under Title 10 and Title 32 of the United States Code.
features:
- description: GoArmyGuard.com and the main recruiting portal allow prospective soldiers to search job listings by MOS, state, and skill, and connect with local recruiters.
  name: Recruiting Portal
- description: Online submission and tracking system for Freedom of Information Act requests to the National Guard Bureau and Army National Guard.
  name: FOIA Request System
- description: Current soldiers access pay, benefits, training records, and deployment orders through the Army self-service portal integrated with the National Guard.
  name: Soldier Self-Service Portal
- description: Public-facing tool allowing citizens to find Army National Guard units and armory locations in their state or territory.
  name: Unit Locator
finops:
- name: Army National Guard Finops
  service_category: API
  slug: army-national-guard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/army-national-guard.png
integrations:
- description: Army National Guard job listings integrate with USAJobs.gov, the federal government's official employment site, for civil service and technician positions.
  name: USA Jobs
- description: Integration with the Army's official benefits counseling portal (myarmybenefits.us.army.mil) for National Guard member benefits information.
  name: MyArmyBenefits
- description: Training management system used by the National Guard to manage soldier training requirements and school seat reservations.
  name: Army Training Requirements and Resources System (ATRRS)
- description: Financial management integration for National Guard pay, travel reimbursement, and benefits payments processed through DFAS.
  name: Defense Finance and Accounting Service (DFAS)
layout: provider
modified: '2026-04-19'
name: Army National Guard
nav: Providers
network: true
overview: 'Army National Guard publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Military, Defense, and National Guard.


  Army National Guard''s developer surface includes developer portal, documentation, and 5 more developer resources.'
plans:
- name: Army National Guard Plans Pricing
  plan_count: 3
  slug: army-national-guard-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Army National Guard Rate Limits
  slug: army-national-guard-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/army-national-guard/refs/heads/main/screenshots/army-national-guard-2026-06-20T172436.png
security:
- kind: domain-security
  name: Army National Guard Domain Security
  slug: army-national-guard-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: army-national-guard
tags:
- Federal-Government
- Military
- Defense
- National Guard
use_cases:
- description: Recruiters and prospective enlistees use the recruiting portal to search available MOS positions, explore benefits, and initiate the enlistment process.
  name: Recruit Prospective Soldiers
- description: Journalists, researchers, and citizens submit Freedom of Information Act requests for Army National Guard records and documents.
  name: Submit FOIA Requests
- description: Citizens and emergency managers find local National Guard units and armory locations for community engagement or emergency coordination.
  name: Locate National Guard Units
- description: Soldiers and their families access information on benefits including education assistance (Montgomery GI Bill), healthcare (TRICARE), and retirement benefits.
  name: Access Soldier Benefits Information
website: https://www.nationalguard.mil/
---
