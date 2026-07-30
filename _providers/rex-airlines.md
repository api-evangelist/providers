---
access_model:
  confidence: high
  label: Accreditation required · No public developer surface
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  - travel-agent-portal
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rex-airlines-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rex-airlines-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.rex.com.au/
- group: start
  title: ''
  type: TravelAgentPortal
  url: https://www.rex.com.au/TravelAgent/Index.aspx
- group: other
  title: ''
  type: TravelAgentRegistration
  url: https://www.rex.com.au/TravelAgent/agentregistration.aspx
- group: start
  title: ''
  type: SignUp
  url: https://www.rex.com.au/TravelAgent/agentregistration.aspx
- group: operate
  title: ''
  type: TravelAgentFAQ
  url: https://www.rex.com.au/TravelAgent/faq.aspx
- group: other
  title: ''
  type: BookingEngine
  url: https://ibe2.rex.com.au/
- group: other
  title: ''
  type: ManageBooking
  url: https://mbe.rex.com.au/
- group: other
  title: ''
  type: FlightSchedules
  url: https://www.rex.com.au/Schedules/default.aspx
- group: other
  title: ''
  type: Network
  url: https://www.rex.com.au/FlightInfo/Network.aspx
- group: other
  title: ''
  type: LoyaltyProgram
  url: https://www.rex.com.au/rexflyer/LoyaltyHomePage.aspx
- group: commercial
  title: ''
  type: LoyaltyTermsOfService
  url: https://www.rex.com.au/rexflyer/RexFlyerTC.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rex.com.au/site_terms.aspx
- group: other
  title: ''
  type: ConditionsOfCarriage
  url: https://www.rex.com.au/FlightInfo/COC.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rex.com.au/privacy.aspx
- group: other
  title: ''
  type: Freight
  url: https://www.rex.com.au/Products_Promo/Freight/Default.aspx
- group: other
  title: ''
  type: Corporate
  url: https://www.rex.com.au/Corporate/
- group: company
  title: ''
  type: About
  url: https://www.rex.com.au/AboutRex/OurCompany/overview.aspx
- group: operate
  title: ''
  type: ContactUs
  url: https://www.rex.com.au/FeedBack/ContactUs.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.rex.com.au/FeedBack/ContactUs.aspx
- group: operate
  title: ''
  type: MediaReleases
  url: https://www.rex.com.au/MediaAndCommunications/
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/regional-express/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/rexairlines
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Rex-116487266942908/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/rex.airlines/
created: '2026-07-28'
description: 'Rex Airlines (Regional Express, IATA ZL / ICAO RXA) is Australia''s second-largest regional carrier, headquartered in Mascot, New South Wales, flying a Saab 340 fleet to roughly 45 regional destinations across every Australian state. Formed in 2002 from the merger of Hazelton and Kendell Airlines, Rex entered voluntary administration in July 2024 and was acquired by US holding company Air T in December 2025 with Australian federal government debt support. In the distribution chain Rex is the inventory owner, not an intermediary — it runs Sabre''s SabreSonic passenger service suite (inventory, reservations, ticketing, ancillaries, check-in) per Sabre''s February 2021 announcement, sells direct through its own ASP.NET booking engine at ibe2.rex.com.au, and reaches trade through a web-only Travel Agent portal gated on an IATA, DAPA or TIDS agency number. Its API posture is honest to state plainly: no developer portal, no public documentation, no OpenAPI, and no NDC claim anywhere
  on rex.com.au. The only published trace of a programmatic interface is a bare "Request API Access" checkbox on the agent registration form — accreditation required, contract unspecified, nothing documented, and no exit path beyond a privacy-law request to the Customer Contact Centre.'
image: https://www.rex.com.au/v8/_lib/menu/img/rexlogo.png
layout: provider
modified: '2026-07-28'
name: Rex Airlines
nav: Providers
network: true
overview: 'Rex Airlines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Australia, Aviation, Airline, and Regional Aviation.


  Rex Airlines'' developer surface includes signup flow, support, and 24 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: domain-security
  name: Rex Airlines Domain Security
  slug: rex-airlines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rex-airlines
tags:
- Travel
- Australia
- Aviation
- Airline
- Regional Aviation
- Distribution
- Booking
- Corporate Travel
- Loyalty
- Freight
website: https://www.rex.com.au/
---
