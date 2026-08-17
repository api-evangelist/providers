---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The agent-facing commerce surface Centric Brands operates across eight of its owned-brand direct-to-consumer storefronts (Hudson Jeans, Joe's Jeans, Favorite Daughter, Buffalo David Bitton, Avirex, He
  name: Centric Brands Owned-Brand Storefront Commerce (UCP / MCP)
  slug: centric-brands-owned-brand-storefront-commerce-ucp-mcp
artifact_total: 44
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/centric-brands-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centric-brands-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/centric-brands-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/centric-brands-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/centric-brands-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/centric-brands-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/centric-brands-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/centric-brands-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/centric-brands-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/centric-brands-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centric-brands-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centricbrands.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centricbrands.com/privacy-policy
- group: other
  title: ''
  type: OwnedBrands
  url: https://www.centricbrands.com/owned-brands
- group: start
  title: ''
  type: Portal
  url: https://www.centricbrands.com
- group: company
  title: ''
  type: About
  url: https://centricbrands.com/about/
- group: other
  title: ''
  type: Leadership
  url: https://centricbrands.com/leadership/
- group: other
  title: ''
  type: Mission
  url: https://centricbrands.com/mission-the-4-cs/
- group: other
  title: ''
  type: Capabilities
  url: https://centricbrands.com/capabilities/
- group: other
  title: ''
  type: Offices
  url: https://centricbrands.com/offices/
- group: company
  title: ''
  type: Blog
  url: https://centricbrands.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://centricbrands.com/press-releases/
- group: company
  title: ''
  type: Careers
  url: https://careers-centricbrands.icims.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/centric-brands
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Centricbrands
- group: other
  title: ''
  type: Philanthropy
  url: https://centricbrands.com/philanthropy/
- group: other
  title: ''
  type: EmployeeResourceGroups
  url: https://centricbrands.com/employee-resource-groups/
- group: other
  title: ''
  type: BrandPortfolio
  url: ''
- group: other
  title: ''
  type: Leadership
  url: ''
- group: other
  title: ''
  type: Offices
  url: ''
- group: other
  title: ''
  type: CorporateHistory
  url: ''
- group: other
  title: ''
  type: NotableAbsences
  url: ''
created: '2026-05-23'
description: 'Centric Brands LLC is a New York-headquartered global lifestyle brand management and product-development platform formed in October 2018 when Differential Brands Group (NASDAQ: DFBG) acquired Global Brands Group''s $1.2B North American licensing business. The company designs, sources, markets, and distributes apparel, accessories, footwear, beauty, and entertainment-licensed products across men''s, women''s, kids'', accessories, and entertainment segments. Its mission is "to be a leading global apparel & accessories company with a portfolio of iconic licensed and owned brands that delight retailers and consumers of all ages." Centric filed for Chapter 11 bankruptcy on May 18, 2020 and emerged in October 2020 under control of secured creditors led by Blackstone''s GSO Capital Partners, Ares Management, and HPS Investment Partners. The company is led by CEO Jason Rabin (since 2018) and operates ~20 global offices across New York (HQ), Los Angeles, Greensboro, Montreal, London,
  Amsterdam, Hong Kong, and multiple cities in China, Bangladesh, Cambodia, India, and Vietnam. Owned brands include Hudson Jeans, Buffalo Jeans, Robert Graham, Joe''s Jeans, Hervé Léger, Favorite Daughter, and AllSaints; licensed apparel brands include Calvin Klein, Tommy Hilfiger, Nautica, Spyder, IZOD, Van Heusen, Kate Spade New York, Coach, Michael Kors, Frye, Timberland, Lucky Brand, Juicy Couture, Under Armour, and Off-White; the entertainment licensing portfolio spans 70+ properties including Disney, Marvel, Warner Bros., DC, Nintendo, Hasbro, Mattel, Nickelodeon, Netflix, Pokémon, Sanrio, Paw Patrol, and the NFL/MLB/NBA/NHL via Sports & Entertainment Licensing. Centric Brands operates "11 end-to-end Ecommerce sites," a 3D design and art studio in Greensboro, and a New York City photo/video studio. Centric Brands runs no corporate developer program - no portal, no API reference, no OpenAPI/AsyncAPI, no SDKs, and no first-party public source (github.com/centric-brands has zero public
  repos; github.com/Centricbrands has one, a third-party fork). Its callable surface is retail, not corporate: as of August 2026 eight Centric-operated owned-brand storefronts serve a live Universal Commerce Protocol (UCP) MCP server at /api/ucp/mcp with 13 anonymous agent tools, advertised via /.well-known/ucp and /llms.txt on every brand host.'
features:
- description: Creative, multi-faceted brand stewardship committed to "protecting our brands' DNA by generating long-term value" for partners and licensors. First of the company's "4 Cs."
  name: Brand Centric
- description: Operational-excellence platform described as "the foundation for a transformational organization – the platform that enables superior end-to-end agility." Second of the "4 Cs."
  name: Business Centric
- description: Consumer-driven product and merchandising model delivering "unparalleled customer solutions that generate remarkable performance and exceptional experiences." Third of the "4 Cs."
  name: Customer Centric
- description: Talent and culture program emphasizing a "dynamic, transparent, and unified culture." Fourth of the "4 Cs."
  name: People Centric
- description: Greensboro, NC creative facility producing 3D design and art assets across the brand portfolio, part of Centric's "expansive creative resources."
  name: 3D Design and Art Studio
- description: New York City "state-of-the-art photo and video studio" used for campaign, e-commerce, and brand content production.
  name: Photo and Video Studio
- description: Direct-to-consumer e-commerce operations running across eleven brand sites with full merchandising, fulfillment, and CX scope.
  name: 11 End-to-End Ecommerce Sites
- description: Diversified Asia-anchored supply chain with offices in Hong Kong, China (Guangzhou, Hangzhou, Qingdao, Shanghai, Shenzhen, Zhuji), Bangladesh, Cambodia, India, and Vietnam. Partnerships with the International Labor Organization and Better Work for compliance.
  name: Global Sourcing Network
- description: Dedicated licensing division (led by Janice Brown since 2018) handling 70+ entertainment, sports, character, and CPG licensed IP for accessories and beauty.
  name: Sports & Entertainment Licensing Group
- description: Regional management hub for Greater China and Southeast Asia sourcing/manufacturing, led by President Marc Compagnon (since March 2022).
  name: Asia Operating Region
- description: European, Middle East, and Africa region with London and Amsterdam offices, led by Managing Director Will van Rensburg.
  name: EMEA Operating Region
- description: Premium-tier division led by Andrew Berg, overseeing labels "including Robert Graham, Avirex, Off White, Herve Leger."
  name: Luxury and Streetwear Division
- description: Operating division led by President Brent Unger since October 2023, covering mainstream lifestyle apparel brands.
  name: Lifestyle Division
- description: Largest single product group, led by Group President Jarrod Kahn since October 2018; spans 40+ licensed and owned accessories brands across handbags, small leather goods, watches, eyewear, hosiery, and headwear.
  name: Accessories Group
- description: Children's apparel division led by President Rob Smith, "responsible for leading the Division across all global brands and categories."
  name: Kids Division
- description: Internal social-compliance team (recently spotlighted in February 2026 news) monitoring factory ethics, labor standards, and ESG criteria across the Asia sourcing base.
  name: Social Compliance Program
image: https://avatars.githubusercontent.com/u/192396914?v=4
integrations:
- description: Wholesale distribution to U.S. mass and mid-tier retailers including Target, Walmart, Kohl's, JCPenney, Macy's, Costco, and Sam's Club.
  name: Mass Retail Distribution
- description: Nordstrom, Bloomingdale's, Saks, Neiman Marcus, Dillard's for premium owned brands and contemporary licensed lines.
  name: Department Store Distribution
- description: TJX (TJ Maxx, Marshalls), Ross, Burlington for off-price and clearance channels.
  name: Specialty / Off-Price Distribution
- description: EMEA and Asia distribution via London, Amsterdam, Hong Kong, and China offices into Europe, Middle East, and APAC retail.
  name: International Wholesale
- description: Long-term royalty agreements with PVH (Calvin Klein, Tommy Hilfiger, IZOD, Van Heusen, Chaps), Authentic Brands Group (Spyder, Juicy Couture, Lucky Brand, Nautica historical), Tapestry (Coach, Kate Spade), Capri (Michael Kors).
  name: Brand Owner Licensors
- description: IP licensing relationships with Disney, Warner Bros. Discovery, NBCUniversal, Paramount, Sony, Netflix, Hasbro, Mattel, Nintendo, Sanrio, Spin Master, MGA Entertainment.
  name: Entertainment Licensors
- description: NFL Properties, MLB Properties, NBA Properties, NHL Enterprises, CLC (College Licensing Company / NCAA), WWE, Monster Jam.
  name: Sports League Licensors
- description: International Labor Organization and Better Work program partnerships for factory monitoring and worker welfare across Asia sourcing base.
  name: Compliance Partnerships
layout: provider
mcp_servers:
- description: ''
  name: centric-brands-mcp.yml
  slug: centric-brands-mcpyml
modified: '2026-08-13'
name: Centric Brands
nav: Providers
network: true
overview: 'Centric Brands publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, Accessories, Footwear, Beauty, and Kids.


  Centric Brands'' developer surface includes authentication, developer portal, engineering blog, and 24 more developer resources.'
plans:
- name: Centric Brands Plans Pricing
  plan_count: 0
  slug: centric-brands-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 0
  name: Centric Brands Rate Limits
  slug: centric-brands-rate-limits
scopes:
- name: Centric Brands Scopes
  scope_count: 4
  slug: centric-brands-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.9
  delta: 13.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 94.4
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 8.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/centric-brands/refs/heads/main/screenshots/centric-brands-2026-06-20T174129.png
security:
- kind: authentication
  name: Centric Brands Authentication
  slug: centric-brands-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Centric Brands Domain Security
  slug: centric-brands-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centric-brands
solutions:
- description: 40+ brand portfolio across handbags, small leather goods, watches, eyewear, hosiery, and headwear; the company's largest division.
  name: Accessories Group
- description: 13 brands including Avirex, MESSI, Buffalo Jeans, Eastside Golf, Hudson Jeans, IZOD, Joe's Jeans, John Elliott, Off-White, Palm Tree Crew, Robert Graham, Airwalk, CAT.
  name: Men's Apparel Portfolio
- description: Buffalo Jeans, Favorite Daughter, Hervé Léger, Hudson Jeans, Joe's Jeans, Palm Tree Crew, Robert Graham - premium and contemporary women's labels.
  name: Women's Apparel Portfolio
- description: 24+ kids' brands including Calvin Klein, Tommy Hilfiger, Nautica, IZOD, Spyder, Lucky Brand, Juicy Couture, Caterpillar, Chaps, Timberland, Under Armour, Van Heusen, Quiksilver, Roxy, RVCA, Dickies, Dockers, Faherty, Gap, Guess, Janie and Jack, Billabong, Hudson, Pastourelle, Blueberi Boulevard, Bass, Kids Headquarters, Off-White, Vingino, CK Baby, Messi, Claire's, A Star Is Born.
  name: Kids Division Portfolio
- description: 70+ entertainment, character, and CPG IPs licensed across accessories, beauty, kids apparel, sleepwear, and bath.
  name: Entertainment Licensed Portfolio
- description: NFL, MLB, NBA, NHL, NCAA, MLS, WWE accessories and headwear.
  name: Sports Licensed Portfolio
- description: 70+ character/CPG IPs adapted to bath, beauty, cosmetics, and personal-care SKUs for mass-market kids and gift channels.
  name: Beauty Portfolio
tags:
- Apparel
- Accessories
- Footwear
- Beauty
- Kids
- Lifestyle
- Brand Management
- Licensing
- Entertainment Licensing
- Sports Licensing
- Fashion
- Consumer Products
- Fortune 1000
- Private Equity Owned
use_cases:
- description: Centric designs, sources, manufactures, and distributes apparel and accessories under multi-year license agreements with brand owners such as Calvin Klein, Tommy Hilfiger, Spyder, and Coach.
  name: Licensed Brand Product Development
- description: Owned brands (Hudson, Buffalo, Robert Graham, Hervé Léger, Joe's Jeans, Favorite Daughter) sold through department stores, specialty retail, and 11 owned e-commerce sites.
  name: Owned-Brand Wholesale & DTC
- description: Manufacturer-of-record for 70+ entertainment IPs producing kids' apparel, beauty, accessories, sleepwear, and hosiery for mass-market and specialty retail.
  name: Entertainment Character Licensing
- description: Sports & Entertainment Licensing Group produces league- licensed accessories and headwear for the major U.S. sports leagues and NCAA.
  name: Sports League / Team Licensing
- description: Centric forms JVs to build new brands - e.g., the January 2026 Palm Tree Crew joint venture (Kygo lifestyle label) and the Claire's strategic licensing partnership.
  name: Strategic Brand Joint Ventures
- description: Inorganic growth via brand acquisitions, e.g., Jennifer Fisher (early 2024); historic portfolio rebuilt post-Chapter 11 around higher-margin owned labels.
  name: Brand Acquisitions
website: https://www.centricbrands.com
---
