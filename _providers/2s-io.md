---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 102
  human_in_the_loop: 2
  name: 2S Io Agentic Access
  operation_count: 575
  slug: 2s-io-agentic-access
  summary_line: 575 operations · 102 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Remote Model Context Protocol server at https://2s.io/mcp (Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo 2s.io 1.0.0). initialize and tools/list answer anonymously with 575 tools
  name: 2s MCP Server
  slug: 2s-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://2s.io/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 1.0.0, provider 2s) advertising a single skil'
  name: 2s A2A Agent
  slug: 2s-a2a-agent
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The agent API from 2s — 1 operation(s) for agent.
  name: 2s Agent API
  slug: 2s-io-agent-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The agriculture API from 2s — 2 operation(s) for agriculture.
  name: 2s Agriculture API
  slug: 2s-io-agriculture-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The ai API from 2s — 16 operation(s) for ai.
  name: 2s AI API
  slug: 2s-io-ai-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The airport API from 2s — 2 operation(s) for airport.
  name: 2s Airport API
  slug: 2s-io-airport-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The aviation API from 2s — 4 operation(s) for aviation.
  name: 2s Aviation API
  slug: 2s-io-aviation-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The bank API from 2s — 1 operation(s) for bank.
  name: 2s Bank API
  slug: 2s-io-bank-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The barcode API from 2s — 1 operation(s) for barcode.
  name: 2s Barcode API
  slug: 2s-io-barcode-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The batch API from 2s — 1 operation(s) for batch.
  name: 2s Batch API
  slug: 2s-io-batch-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The bio API from 2s — 3 operation(s) for bio.
  name: 2s Bio API
  slug: 2s-io-bio-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The bls API from 2s — 1 operation(s) for bls.
  name: 2s Bls API
  slug: 2s-io-bls-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The book API from 2s — 1 operation(s) for book.
  name: 2s Book API
  slug: 2s-io-book-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The business API from 2s — 16 operation(s) for business.
  name: 2s Business API
  slug: 2s-io-business-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The calendar API from 2s — 4 operation(s) for calendar.
  name: 2s Calendar API
  slug: 2s-io-calendar-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The census API from 2s — 2 operation(s) for census.
  name: 2s Census API
  slug: 2s-io-census-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The chem API from 2s — 1 operation(s) for chem.
  name: 2s Chem API
  slug: 2s-io-chem-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The chinese API from 2s — 3 operation(s) for chinese.
  name: 2s Chinese API
  slug: 2s-io-chinese-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The class API from 2s — 1 operation(s) for class.
  name: 2s Class API
  slug: 2s-io-class-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The climate API from 2s — 2 operation(s) for climate.
  name: 2s Climate API
  slug: 2s-io-climate-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The clinical API from 2s — 2 operation(s) for clinical.
  name: 2s Clinical API
  slug: 2s-io-clinical-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The code API from 2s — 1 operation(s) for code.
  name: 2s Code API
  slug: 2s-io-code-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The convert API from 2s — 2 operation(s) for convert.
  name: 2s Convert API
  slug: 2s-io-convert-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The countdown API from 2s — 1 operation(s) for countdown.
  name: 2s Countdown API
  slug: 2s-io-countdown-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The country API from 2s — 2 operation(s) for country.
  name: 2s Country API
  slug: 2s-io-country-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The crypto API from 2s — 46 operation(s) for crypto.
  name: 2s Crypto API
  slug: 2s-io-crypto-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The dev API from 2s — 15 operation(s) for dev.
  name: 2s Dev API
  slug: 2s-io-dev-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The dns API from 2s — 1 operation(s) for dns.
  name: 2s Dns API
  slug: 2s-io-dns-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The domain API from 2s — 4 operation(s) for domain.
  name: 2s Domain API
  slug: 2s-io-domain-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The earth API from 2s — 2 operation(s) for earth.
  name: 2s Earth API
  slug: 2s-io-earth-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The econ API from 2s — 10 operation(s) for econ.
  name: 2s Econ API
  slug: 2s-io-econ-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The edi API from 2s — 5 operation(s) for edi.
  name: 2s Edi API
  slug: 2s-io-edi-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The edu API from 2s — 2 operation(s) for edu.
  name: 2s Edu API
  slug: 2s-io-edu-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The email API from 2s — 1 operation(s) for email.
  name: 2s Email API
  slug: 2s-io-email-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The energy API from 2s — 8 operation(s) for energy.
  name: 2s Energy API
  slug: 2s-io-energy-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The factcheck API from 2s — 1 operation(s) for factcheck.
  name: 2s Factcheck API
  slug: 2s-io-factcheck-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The feedback API from 2s — 1 operation(s) for feedback.
  name: 2s Feedback API
  slug: 2s-io-feedback-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The finance API from 2s — 17 operation(s) for finance.
  name: 2s Finance API
  slug: 2s-io-finance-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The flight API from 2s — 3 operation(s) for flight.
  name: 2s Flight API
  slug: 2s-io-flight-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The food API from 2s — 2 operation(s) for food.
  name: 2s Food API
  slug: 2s-io-food-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The fx API from 2s — 2 operation(s) for fx.
  name: 2s Fx API
  slug: 2s-io-fx-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The geo API from 2s — 7 operation(s) for geo.
  name: 2s Geo API
  slug: 2s-io-geo-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The geocode API from 2s — 2 operation(s) for geocode.
  name: 2s Geocode API
  slug: 2s-io-geocode-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The github API from 2s — 14 operation(s) for github.
  name: 2s GitHub API
  slug: 2s-io-github-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The gov API from 2s — 56 operation(s) for gov.
  name: 2s Gov API
  slug: 2s-io-gov-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The hash API from 2s — 1 operation(s) for hash.
  name: 2s Hash API
  slug: 2s-io-hash-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The health API from 2s — 7 operation(s) for health.
  name: 2s Health API
  slug: 2s-io-health-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The html API from 2s — 1 operation(s) for html.
  name: 2s Html API
  slug: 2s-io-html-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The image API from 2s — 1 operation(s) for image.
  name: 2s Image API
  slug: 2s-io-image-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The inflation API from 2s — 4 operation(s) for inflation.
  name: 2s Inflation API
  slug: 2s-io-inflation-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The ipinfo API from 2s — 1 operation(s) for ipinfo.
  name: 2s Ipinfo API
  slug: 2s-io-ipinfo-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The iso API from 2s — 3 operation(s) for iso.
  name: 2s Iso API
  slug: 2s-io-iso-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The job API from 2s — 2 operation(s) for job.
  name: 2s Job API
  slug: 2s-io-job-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The labor API from 2s — 3 operation(s) for labor.
  name: 2s Labor API
  slug: 2s-io-labor-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The law API from 2s — 12 operation(s) for law.
  name: 2s Law API
  slug: 2s-io-law-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The license API from 2s — 4 operation(s) for license.
  name: 2s License API
  slug: 2s-io-license-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The lock API from 2s — 3 operation(s) for lock.
  name: 2s Lock API
  slug: 2s-io-lock-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The maritime API from 2s — 3 operation(s) for maritime.
  name: 2s Maritime API
  slug: 2s-io-maritime-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The markets API from 2s — 2 operation(s) for markets.
  name: 2s Markets API
  slug: 2s-io-markets-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The medical API from 2s — 14 operation(s) for medical.
  name: 2s Medical API
  slug: 2s-io-medical-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The music API from 2s — 3 operation(s) for music.
  name: 2s Music API
  slug: 2s-io-music-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The net API from 2s — 4 operation(s) for net.
  name: 2s Net API
  slug: 2s-io-net-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The news API from 2s — 5 operation(s) for news.
  name: 2s News API
  slug: 2s-io-news-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The nonprofit API from 2s — 2 operation(s) for nonprofit.
  name: 2s Nonprofit API
  slug: 2s-io-nonprofit-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The nutrition API from 2s — 1 operation(s) for nutrition.
  name: 2s Nutrition API
  slug: 2s-io-nutrition-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The occupation API from 2s — 3 operation(s) for occupation.
  name: 2s Occupation API
  slug: 2s-io-occupation-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The paper API from 2s — 1 operation(s) for paper.
  name: 2s Paper API
  slug: 2s-io-paper-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The papers API from 2s — 2 operation(s) for papers.
  name: 2s Papers API
  slug: 2s-io-papers-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The park API from 2s — 1 operation(s) for park.
  name: 2s Park API
  slug: 2s-io-park-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The patents API from 2s — 7 operation(s) for patents.
  name: 2s Patents API
  slug: 2s-io-patents-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The person API from 2s — 1 operation(s) for person.
  name: 2s Person API
  slug: 2s-io-person-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The phone API from 2s — 1 operation(s) for phone.
  name: 2s Phone API
  slug: 2s-io-phone-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The poi API from 2s — 1 operation(s) for poi.
  name: 2s Poi API
  slug: 2s-io-poi-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The predict API from 2s — 23 operation(s) for predict.
  name: 2s Predict API
  slug: 2s-io-predict-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The product API from 2s — 1 operation(s) for product.
  name: 2s Product API
  slug: 2s-io-product-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The property API from 2s — 4 operation(s) for property.
  name: 2s Property API
  slug: 2s-io-property-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The pubsub API from 2s — 4 operation(s) for pubsub.
  name: 2s Pubsub API
  slug: 2s-io-pubsub-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The quakes API from 2s — 1 operation(s) for quakes.
  name: 2s Quakes API
  slug: 2s-io-quakes-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The queue API from 2s — 4 operation(s) for queue.
  name: 2s Queue API
  slug: 2s-io-queue-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The recreation API from 2s — 1 operation(s) for recreation.
  name: 2s Recreation API
  slug: 2s-io-recreation-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The registry API from 2s — 2 operation(s) for registry.
  name: 2s Registry API
  slug: 2s-io-registry-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The research API from 2s — 3 operation(s) for research.
  name: 2s Research API
  slug: 2s-io-research-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The schedule API from 2s — 3 operation(s) for schedule.
  name: 2s Schedule API
  slug: 2s-io-schedule-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The search API from 2s — 5 operation(s) for search.
  name: 2s Search API
  slug: 2s-io-search-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The security API from 2s — 16 operation(s) for security.
  name: 2s Security API
  slug: 2s-io-security-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The soil API from 2s — 2 operation(s) for soil.
  name: 2s Soil API
  slug: 2s-io-soil-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The space API from 2s — 11 operation(s) for space.
  name: 2s Space API
  slug: 2s-io-space-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The sports API from 2s — 11 operation(s) for sports.
  name: 2s Sports API
  slug: 2s-io-sports-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The stocks API from 2s — 14 operation(s) for stocks.
  name: 2s Stocks API
  slug: 2s-io-stocks-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The store API from 2s — 16 operation(s) for store.
  name: 2s Store API
  slug: 2s-io-store-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The sunrise API from 2s — 1 operation(s) for sunrise.
  name: 2s Sunrise API
  slug: 2s-io-sunrise-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The tax API from 2s — 2 operation(s) for tax.
  name: 2s Tax API
  slug: 2s-io-tax-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The tcg API from 2s — 4 operation(s) for tcg.
  name: 2s Tcg API
  slug: 2s-io-tcg-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The telecom API from 2s — 2 operation(s) for telecom.
  name: 2s Telecom API
  slug: 2s-io-telecom-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The text API from 2s — 1 operation(s) for text.
  name: 2s Text API
  slug: 2s-io-text-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The tides API from 2s — 1 operation(s) for tides.
  name: 2s Tides API
  slug: 2s-io-tides-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The time API from 2s — 1 operation(s) for time.
  name: 2s Time API
  slug: 2s-io-time-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The timezone API from 2s — 1 operation(s) for timezone.
  name: 2s Timezone API
  slug: 2s-io-timezone-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The tld API from 2s — 1 operation(s) for tld.
  name: 2s Tld API
  slug: 2s-io-tld-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The tls API from 2s — 1 operation(s) for tls.
  name: 2s Tls API
  slug: 2s-io-tls-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The trade API from 2s — 4 operation(s) for trade.
  name: 2s Trade API
  slug: 2s-io-trade-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The transcribe API from 2s — 1 operation(s) for transcribe.
  name: 2s Transcribe API
  slug: 2s-io-transcribe-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The travel API from 2s — 2 operation(s) for travel.
  name: 2s Travel API
  slug: 2s-io-travel-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The treasury API from 2s — 4 operation(s) for treasury.
  name: 2s Treasury API
  slug: 2s-io-treasury-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The url API from 2s — 4 operation(s) for url.
  name: 2s URL API
  slug: 2s-io-url-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The validate API from 2s — 10 operation(s) for validate.
  name: 2s Validate API
  slug: 2s-io-validate-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The vehicle API from 2s — 11 operation(s) for vehicle.
  name: 2s Vehicle API
  slug: 2s-io-vehicle-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The watchers API from 2s — 27 operation(s) for watchers.
  name: 2s Watchers API
  slug: 2s-io-watchers-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The water API from 2s — 1 operation(s) for water.
  name: 2s Water API
  slug: 2s-io-water-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The weather API from 2s — 8 operation(s) for weather.
  name: 2s Weather API
  slug: 2s-io-weather-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The wikidata API from 2s — 1 operation(s) for wikidata.
  name: 2s Wikidata API
  slug: 2s-io-wikidata-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The wikipedia API from 2s — 1 operation(s) for wikipedia.
  name: 2s Wikipedia API
  slug: 2s-io-wikipedia-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The word API from 2s — 2 operation(s) for word.
  name: 2s Word API
  slug: 2s-io-word-api
- baseURL: https://2s.io/mcp
  baseurl_source: declared
  description: The worldbank API from 2s — 1 operation(s) for worldbank.
  name: 2s Worldbank API
  slug: 2s-io-worldbank-api
artifact_total: 122
asyncapis:
- description: ''
  name: 2S Io Watchers Webhooks
  slug: 2s-io-watchers-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/overlays/2s-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/2s-io-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://2s.io/
- group: docs
  title: ''
  type: Documentation
  url: https://2s.io/learn/x402
- group: docs
  title: ''
  type: APIReference
  url: https://2s.io/discover
- group: start
  title: ''
  type: GettingStarted
  url: https://2s.io/learn/x402/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://2s.io/discover
- group: operate
  title: ''
  type: StatusPage
  url: https://2s.io/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/changelog/2s-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/2s-io-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://2s.io/changelog.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/2s-io
- group: operate
  title: ''
  type: Support
  url: https://github.com/2s-io/sdk/issues
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/a2a/2s-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/2s-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/mcp/2s-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/2s-io-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/llms/2s-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/2s-io-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/well-known/2s-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/2s-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/well-known/2s-io-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/2s-io-api-catalog.json
- group: other
  title: ''
  type: APIsJson
  url: https://2s.io/apis.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/well-known/2s-io-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/2s-io-ai-plugin.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/packages/2s-io-packages.yml
  title: ''
  type: Packages
  url: packages/2s-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/packages/2s-io-packages.yml
  title: ''
  type: SDKs
  url: packages/2s-io-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/authentication/2s-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/2s-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/conventions/2s-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/2s-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/conventions/2s-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/2s-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/errors/2s-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/2s-io-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/rate-limits/2s-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/2s-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/plans/2s-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/2s-io-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/sandbox/2s-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/2s-io-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/conformance/2s-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/2s-io-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/lifecycle/2s-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/2s-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/asyncapi/2s-io-watchers-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/2s-io-watchers-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/agentic-access/2s-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/2s-io-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/data-model/2s-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/2s-io-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/security/2s-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/2s-io-domain-security.yml
created: '2026-09-19'
description: '2s ("the (most) everything API", 2s.io) is a pay-per-call REST API built for AI agents: 575 endpoints across 112 groups on one origin — US public records and government data, company and legal identifiers (GLEIF, OFAC, state registries), SEC filings, crypto and web3, security and CVEs, patents and case law, medical codes, weather and geocoding, ANSI X12 / EDIFACT EDI, an OpenAI-compatible AI gateway (chat, image, multi-model council) and wallet-scoped agent infrastructure (kv/doc/vector/blob store, locks, queues, schedules, pub/sub and 26 kinds of signed-callback watchers). There are no accounts and no API keys: every call is paid in USDC on Base or Solana through the x402 protocol (HTTP 402 → sign → retry), with a free trial call per endpoint per hour and actual-usage "upto" billing on AI endpoints. The same catalog is published as an OpenAPI 3.1.0 contract at https://2s.io/openapi.json, a remote MCP server at https://2s.io/mcp (plus the npx @2sio/mcp local server), an A2A
  0.3.0 agent card whose one skill is endpoint discovery, an RFC 9727 API catalog, an APIs.json index, an llms.txt, an MCP server card, an x402 manifest and an ERC-8004 on-chain agent registration. Maintained by an individual operator (alley@2s.io); the SDK monorepo is github.com/2s-io/sdk.'
image: https://2s.io/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: 2s MCP Server
  slug: 2s-mcp-server
- description: ''
  name: 2s hosted MCP endpoint (Streamable HTTP)
  slug: 2s-hosted-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: 2s
nav: Providers
network: true
overview: '2s publishes 114 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Agriculture API, AI API, and 111 more. Tagged areas include Agents, Agentic Commerce, x402, MCP, and A2A.


  The 2s catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  2s'' developer surface includes documentation, API reference, getting-started guide, pricing, changelog, support, authentication, and 27 more developer resources.'
plans:
- name: 2S Io Plans Pricing
  plan_count: 0
  slug: 2s-io-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: 2S Io Rate Limits
  slug: 2s-io-rate-limits
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 66.7
    discoverability: 75.0
    operational_transparency: 76.3
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 112
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 50.0
security:
- kind: authentication
  name: 2S Io Authentication
  slug: 2s-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: 2S Io Domain Security
  slug: 2s-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 2s-io
tags:
- Agents
- Agentic Commerce
- x402
- MCP
- A2A
- Public Records
- Government Data
- Finance
- Crypto
- Security
- Legal
- Weather
- Geocoding
- EDI
- AI Gateway
- Agent Infrastructure
- Webhook
- Agent-Native
website: https://2s.io/
---
