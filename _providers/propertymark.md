---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/propertymark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://pixl8.com/en/vulnerability-disclosure-policy.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propertymark-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/propertymark-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/propertymark-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/propertymark-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.propertymark.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.propertymark.co.uk/about-us.html
- group: other
  title: ''
  type: Standards
  url: https://www.propertymark.co.uk/professional-standards.html
- group: other
  title: ''
  type: Standards
  url: https://www.propertymark.co.uk/professional-standards/rules.html
- group: design
  title: ''
  type: Rules
  url: https://www.propertymark.co.uk/asset/1B740FBB%2D8CC0%2D4ED4%2D8A5BD9B5D006D765/
- group: auth
  title: ''
  type: Certification
  url: https://www.propertymark.co.uk/professional-standards/rules/cmp.html
- group: auth
  title: ''
  type: Certification
  url: https://www.propertymark.co.uk/professional-standards/cmp-applications.html
- group: other
  title: ''
  type: Directory
  url: https://www.propertymark.co.uk/find-an-expert.html
- group: company
  title: ''
  type: Partners
  url: https://www.propertymark.co.uk/membership/industry-suppliers.html
- group: other
  title: ''
  type: Membership
  url: https://www.propertymark.co.uk/membership.html
- group: start
  title: ''
  type: SignUp
  url: https://www.propertymark.co.uk/membership/join.html
- group: start
  title: ''
  type: Login
  url: https://www.propertymark.co.uk/login.html
- group: other
  title: ''
  type: Education
  url: https://www.propertymark.co.uk/pmq.html
- group: start
  title: ''
  type: Portal
  url: https://learnerportal.propertymark.co.uk/
- group: other
  title: ''
  type: Complaints
  url: https://www.propertymark.co.uk/professional-standards/complaints.html
- group: other
  title: ''
  type: Policy
  url: https://www.propertymark.co.uk/policy.html
- group: company
  title: ''
  type: NewsAndReports
  url: https://www.propertymark.co.uk/news-reports.html
- group: company
  title: ''
  type: Blog
  url: https://www.propertymark.co.uk/news-reports/latest.html
- group: other
  title: ''
  type: Podcast
  url: https://www.propertymark.co.uk/news-reports/podcast.html
- group: operate
  title: ''
  type: Support
  url: https://www.propertymark.co.uk/membership/helpline.html
- group: other
  title: ''
  type: Referrals
  url: https://www.propertymark.co.uk/advantage/connect.html
- group: company
  title: ''
  type: Jobs
  url: https://jobs.propertymark.co.uk/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.propertymark.co.uk/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://pixl8.com/en/vulnerability-disclosure-policy.html
- group: other
  title: ''
  type: Sitemap
  url: https://www.propertymark.co.uk/sitemap.xml
- group: other
  title: ''
  type: Robots
  url: https://www.propertymark.co.uk/robots.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.propertymark.co.uk/privacy-policy.html
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.propertymark.co.uk/cookie-policy.html
- group: operate
  title: ''
  type: Contact
  url: https://www.propertymark.co.uk/contact.html
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCwPUqKRQZ7ezBwbc0yrOjxQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/propertymark/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/PropertymarkUK/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/propertymarkuk
created: '2026-07-26'
description: 'Propertymark is the United Kingdom''s largest professional body for property agents, formed in 2017 from the merger of the National Association of Estate Agents (NAEA), the Association of Residential Letting Agents (ARLA), the Institute of Commercial and Business Agents (ICBA) and the National Association of Valuers and Auctioneers (NAVA), and representing "over 19,000 members" across residential sales, lettings, commercial property, inventories, auctions and valuation. Its home market is the United Kingdom - England, Scotland, Wales, Northern Ireland and the Channel Islands. In the property value chain it sits on the agent-accreditation and consumer-protection side, not the listings side: it publishes the Conduct and Membership Rules, operates a government-approved Client Money Protection scheme, runs Propertymark Qualifications as the sector''s specialist awarding organisation, and lobbies government on estate and letting agency regulation. Its API posture is the flat, honest
  zero. There is no developer portal, no documented API, no SDK, no webhooks and no published machine-readable contract of any kind: developer.propertymark.co.uk, developers.propertymark.co.uk, api.propertymark.co.uk, data.propertymark.co.uk and standards.propertymark.co.uk all fail DNS resolution, and /openapi.json, /swagger.json, /api-docs, /api, /developers, /docs, /$metadata and /odata all return honest HTTP 404s from www.propertymark.co.uk. RESO is entirely absent - the site''s own search returns "result: 0 of 0" for both "RESO" and "OData" - because the United Kingdom has no MLS and therefore no listing-data certification layer to be certified against; UK residential listings reach consumers through the Rightmove/Zoopla portal duopoly via agency CRM software, several of whose vendors (Reapit, Street, MRI Software, Dezrez, AgentOS, Coadjute, and Rightmove itself) appear in Propertymark''s own Industry Supplier directory. What Propertymark does publish freely is its rulebook: the Propertymark
  Conduct and Membership Rules PDF downloads anonymously with no login and no EULA. Its only machine-readable surface is undocumented - an internal Preside CMS JSON endpoint behind the public Find an Expert member directory - and its member area is SAML-gated, returning HTTP 401. Genuinely open UK property data comes from HM Land Registry and Ordnance Survey, not from the agents'' professional body.'
image: https://www.propertymark.co.uk/static/088fd899-9b36-4cd5-b685175e6c489b92/222x87_highestperformance__4a7c7e45a350/Propertymark-Company-logo.png
layout: provider
modified: '2026-07-26'
name: Propertymark
nav: Providers
network: true
overview: 'Propertymark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United Kingdom, Industry Body, Estate Agents, and Rentals.


  Propertymark''s developer surface includes signup flow, developer portal, engineering blog, support, YouTube channel, and 34 more developer resources.'
random_paper: 85
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 17.5
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Propertymark Domain Security
  slug: propertymark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Propertymark Vulnerability Disclosure
  slug: propertymark-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: propertymark
tags:
- Real Estate
- United Kingdom
- Industry Body
- Estate Agents
- Rentals
- Property Management
- Standards
- Certification
- Client Money Protection
- Commercial Real Estate
- Valuation
- PropTech
website: https://www.propertymark.co.uk/
---
