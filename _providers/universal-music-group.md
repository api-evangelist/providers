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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Authenticated royalty statement portal for UMG-distributed artists and labels. Provides login-gated access to royalty statements, statement history, and supporting documentation. The portal is deliver
  name: UMG Royalty Portal
  slug: umg-royalty-portal
- description: Universal Music Publishing Group's songwriter and client royalty portal, providing real-time access to earnings, statements, registrations, and catalog data for UMPG-signed songwriters and publisher a
  name: UMPG Window
  slug: umpg-window
- description: Bravado is UMG's global merchandise and brand-management division, operating direct-to-consumer artist merchandise storefronts and tour merchandise for UMG's roster. Each artist store is delivered via
  name: Bravado Merchandise Storefronts
  slug: bravado-merch
- description: 7digital operates a B2B catalog and media-delivery API that includes UMG-licensed recordings for hackathon and partner use. This is the closest thing to a publicly documented developer surface for UMG
  name: 7digital UMG Catalog API (Partner Surface)
  slug: partner-7digital
- description: Official UMG GitHub organization (login Universal-Music-Group, org id 169924279), created May 15, 2024. As of profiling, the org has 0 public repositories, 0 public gists, 0 followers, no bio, no blog
  name: Universal-Music-Group GitHub Organization
  slug: github-org
artifact_total: 34
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/api-evangelist/universal-music-group/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/api-evangelist/universal-music-group/tree/main/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universal-music-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.universalmusic.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.universalmusic.com/about/
- group: company
  title: ''
  type: News
  url: https://www.universalmusic.com/news/
- group: other
  title: ''
  type: Labels
  url: https://www.universalmusic.com/labels/
- group: company
  title: ''
  type: Careers
  url: https://www.universalmusic.com/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.universalmusic.com/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.universalmusic.com/investors/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.universalmusic.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.universalmusic.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/universalmusicgroup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Universal-Music-Group
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/api-evangelist/universal-music-group
- group: other
  title: ''
  type: Stock
  url: https://live.euronext.com/en/product/equities/NL0015000IY2-XAMS
- group: other
  title: ''
  type: ParentCompany
  url: ''
- group: other
  title: ''
  type: Subsidiary
  url: ''
- group: other
  title: ''
  type: LabelFamily
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.universalmusic.com/feed/
created: '2026-05-23'
description: 'Universal Music Group N.V. (UMG) is the world''s largest music company, headquartered in Hilversum, Netherlands with operational headquarters in Santa Monica, California. Spun off from Vivendi and listed on Euronext Amsterdam (ticker: UMG) on September 21, 2021 at a EUR 54 billion valuation, UMG operates Recorded Music, Music Publishing (Universal Music Publishing Group / UMPG), and Merchandising (Bravado), plus film and television production (PolyGram Entertainment) and the artist services and catalog arm Universal Music Enterprises. The company is led by Chairman and CEO Sir Lucian Grainge. Major label families include Republic Corps (Republic, Island, Def Jam), Interscope Capitol Labels Group (Interscope, Geffen, A&M, Capitol, Blue Note, Motown), Virgin Music Group, Verve Label Group (Verve, Decca, Deutsche Grammophon, Impulse!, Philips), UMG Nashville (MCA Nashville, Mercury Nashville, EMI Records Nashville, Capitol Records Nashville), Universal Music Latin Entertainment,
  and Universal Music UK. Catalog scale exceeds 3 million recordings and 4 million compositions. Ownership is split among Bolloré / Vivendi (~28%), Tencent Music (~11%), Pershing Square (~10%), and the public float. UMG operates no public developer portal: catalog and metadata reach developers only indirectly through downstream DSPs (Spotify, Apple Music, YouTube, Amazon Music) and through partner / aggregator programs (7digital exposed UMG catalog under a partner API; that integration is the only third-party developer-facing surface that has ever been openly documented). Royalty and publishing portals (UMG Royalty Portal, UMPG Window) exist for songwriters and rights holders behind authentication, not as APIs. AI is the active integration vector in 2025-2026: UMG has announced licensed generative-music partnerships with Udio, Splice, KLAY Vision, SoundLabs, ProRata, BandLab, YouTube, TikTok, Meta, and KDDI, and has filed 15+ AI patents with Liquidax Capital across collaboration, rights
  management, music & health, and AI threat protection. These integrations operate through bilateral commercial agreements, not a self-serve developer program. The official Universal-Music-Group GitHub organization (created May 15, 2024) has 0 public repositories.'
features:
- description: Over 3 million recordings spanning UMG's label families, distributed to DSPs via private DDEX-based ingest pipelines.
  name: Recorded Music Catalog
- description: Over 4 million compositions administered by Universal Music Publishing Group across writer signings and acquired catalogs.
  name: Music Publishing Catalog
- description: Direct-to-consumer artist merchandise storefronts and tour merch operated by the Bravado division.
  name: Merchandise (Bravado)
- description: Music-led films, documentaries, and series produced under PolyGram Entertainment and Mercury Studios.
  name: Film and Television
- description: Authenticated royalty-statement portals (UMG Royalty Portal for recordings, UMPG Window for publishing) for artists, labels, and songwriters.
  name: Royalty Portals
- description: Commercial AI-music licensing program covering Udio, Splice, SoundLabs, KLAY Vision, ProRata, BandLab, YouTube, TikTok, Meta, and KDDI.
  name: Licensed AI Partnerships
- description: 15+ AI patents filed with Liquidax Capital spanning collaboration, multimedia content, music & health, AI threat protection, and rights management.
  name: AI Patent Portfolio
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universal-music-group.png
integrations:
- description: Industry-standard messaging suite (ERN for release notification, RIN for recording information, MEAD for media-enrichment, DSR for sales reporting) used by UMG to deliver content to DSPs.
  name: DDEX
  url: https://ddex.net/
- description: Catalog delivered to Spotify via DDEX; developers query UMG catalog through Spotify Web API rather than any UMG-branded API.
  name: Spotify
- description: Catalog delivered to Apple Music; downstream developer access via Apple Music API.
  name: Apple Music
- description: Catalog and AI Music Principles partnership covering UGC matching, music identification, and licensed AI-music experiments.
  name: YouTube / YouTube Music
- description: Licensed music partnership covering catalog availability and AI-related provisions.
  name: TikTok
- description: Licensed music agreements covering Facebook, Instagram, and emerging AI surfaces.
  name: Meta
- description: Japan telecom partner; AI-related licensed-music agreement.
  name: KDDI
- description: Licensed generative-AI music platform; UMG strategic partner under Artist Centric AI framework.
  name: Udio
- description: AI music-tools partner for UMG-roster artist tooling.
  name: Splice
- description: Voice-model and AI-music partner.
  name: SoundLabs
- description: AI-music platform partner.
  name: KLAY Vision
- description: AI training / rights attribution partner.
  name: ProRata
- description: Partner on ethical-AI framework for songwriters and artists (Oct 2023 agreement).
  name: BandLab Technologies
- description: IP asset-management and advisory firm co-developing UMG's AI patent portfolio (15+ filings).
  name: Liquidax Capital
- description: Partner aggregator that exposes UMG catalog under a B2B API used in hackathons and embedded media partners.
  name: 7digital
- description: UMG runs Drupal-based corporate properties (organization listed at drupal.org/UMG).
  name: Drupal
layout: provider
modified: '2026-07-25'
name: Universal Music Group
nav: Providers
network: true
overview: 'Universal Music Group publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Licensing, Big Three, Catalog, Entertainment, and Generative Music.


  Universal Music Group''s developer surface includes product news, engineering blog, and 15 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/universal-music-group/refs/heads/main/screenshots/universal-music-group-2026-06-20T200122.png
security:
- kind: domain-security
  name: Universal Music Group Domain Security
  slug: universal-music-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: universal-music-group
tags:
- AI Licensing
- Big Three
- Catalog
- Entertainment
- Generative Music
- Licensing
- Major Label
- Merchandising
- Music
- Music Publishing
- Recorded Music
- Royalties
- Streaming
use_cases:
- description: End-user and developer access to UMG's recorded-music catalog occurs through downstream DSPs (Spotify, Apple Music, YouTube Music, Amazon Music, Tidal), each of which publishes its own developer API.
  name: Streaming Catalog Access
- description: Film, TV, advertising, and game producers license UMG recordings and UMPG compositions through bilateral business-affairs negotiation, not through a self-serve API.
  name: Sync Licensing
- description: Artists, labels, and songwriters access royalty statements through the authenticated UMG Royalty Portal and UMPG Window apps.
  name: Royalty Reporting
- description: Licensed AI platforms (Udio, Splice, SoundLabs, etc.) access UMG content under bilateral commercial agreements that govern training, generation, and downstream remixing rights.
  name: AI Training and Generation Licensing
- description: Direct-to-consumer fan commerce operated by Bravado on behalf of UMG's artist roster.
  name: Merchandise Distribution
website: https://www.universalmusic.com
---
