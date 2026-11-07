---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Remote MCP server (JSON-RPC 2.0 over Streamable HTTP) at https://emem.dev/mcp exposing 110 tools; /mcp lists an 18-tool core loop and /mcp/full the complete set. No authentication to read; every tool '
  name: emem MCP Server
  slug: emem-mcp-server
- description: 'Agent-to-agent surface: synchronous JSON-RPC message/send at POST /a2a/tasks, an async task extension at /v1/a2a/tasks with polling and cancel, and a skill query at /v1/a2a/skills. Every MCP tool is p'
  name: emem A2A Agent
  slug: emem-a2a-agent
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The A2a API from emem — 7 operation(s) for a2a.
  name: emem A2a API
  slug: emem-dev-a2a-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Agent Card API from emem — 1 operation(s) for agent card.
  name: emem Agent Card API
  slug: emem-dev-agent-card-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Agent Stats API from emem — 1 operation(s) for agent stats.
  name: emem Agent Stats API
  slug: emem-dev-agent-stats-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Algorithms API from emem — 2 operation(s) for algorithms.
  name: emem Algorithms API
  slug: emem-dev-algorithms-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Artifacts API from emem — 1 operation(s) for artifacts.
  name: emem Artifacts API
  slug: emem-dev-artifacts-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Ask API from emem — 1 operation(s) for ask.
  name: emem Ask API
  slug: emem-dev-ask-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Attest API from emem — 1 operation(s) for attest.
  name: emem Attest API
  slug: emem-dev-attest-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Attest Cbor API from emem — 1 operation(s) for attest cbor.
  name: emem Attest Cbor API
  slug: emem-dev-attest-cbor-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Attest Traced API from emem — 1 operation(s) for attest traced.
  name: emem Attest Traced API
  slug: emem-dev-attest-traced-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Backfill API from emem — 1 operation(s) for backfill.
  name: emem Backfill API
  slug: emem-dev-backfill-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Band Composite API from emem — 1 operation(s) for band composite.
  name: emem Band Composite API
  slug: emem-dev-band-composite-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Band Cube API from emem — 1 operation(s) for band cube.
  name: emem Band Cube API
  slug: emem-dev-band-cube-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Band Raster API from emem — 1 operation(s) for band raster.
  name: emem Band Raster API
  slug: emem-dev-band-raster-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Bands API from emem — 1 operation(s) for bands.
  name: emem Bands API
  slug: emem-dev-bands-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Benchmark API from emem — 2 operation(s) for benchmark.
  name: emem Benchmark API
  slug: emem-dev-benchmark-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The boring API from emem — 10 operation(s) for boring.
  name: emem Boring API
  slug: emem-dev-boring-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Burn Severity API from emem — 1 operation(s) for burn severity.
  name: emem Burn Severity API
  slug: emem-dev-burn-severity-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Capabilities API from emem — 1 operation(s) for capabilities.
  name: emem Capabilities API
  slug: emem-dev-capabilities-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Cells API from emem — 6 operation(s) for cells.
  name: emem Cells API
  slug: emem-dev-cells-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Cells In Bbox API from emem — 1 operation(s) for cells in bbox.
  name: emem Cells In Bbox API
  slug: emem-dev-cells-in-bbox-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Change Attribution API from emem — 1 operation(s) for change attribution.
  name: emem Change Attribution API
  slug: emem-dev-change-attribution-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The cite API from emem — 4 operation(s) for cite.
  name: emem Cite API
  slug: emem-dev-cite-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Compare API from emem — 1 operation(s) for compare.
  name: emem Compare API
  slug: emem-dev-compare-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Compare Bands API from emem — 1 operation(s) for compare bands.
  name: emem Compare Bands API
  slug: emem-dev-compare-bands-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Compare Same Doy API from emem — 1 operation(s) for compare same doy.
  name: emem Compare Same Doy API
  slug: emem-dev-compare-same-doy-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The compliance API from emem — 1 operation(s) for compliance.
  name: emem Compliance API
  slug: emem-dev-compliance-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The contradiction-detection API from emem — 1 operation(s) for contradiction-detection.
  name: emem Contradiction Detection API
  slug: emem-dev-contradiction-detection-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Contributors API from emem — 2 operation(s) for contributors.
  name: emem Contributors API
  slug: emem-dev-contributors-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Corpus State Stats API from emem — 1 operation(s) for corpus state stats.
  name: emem Corpus State Stats API
  slug: emem-dev-corpus-state-stats-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Coverage API from emem — 1 operation(s) for coverage.
  name: emem Coverage API
  slug: emem-dev-coverage-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Coverage Map.svg API from emem — 1 operation(s) for coverage map.svg.
  name: emem Coverage Map.svg API
  slug: emem-dev-coverage-map-svg-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Coverage Matrix API from emem — 1 operation(s) for coverage matrix.
  name: emem Coverage Matrix API
  slug: emem-dev-coverage-matrix-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Cube API from emem — 1 operation(s) for cube.
  name: emem Cube API
  slug: emem-dev-cube-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Data Availability API from emem — 1 operation(s) for data availability.
  name: emem Data Availability API
  slug: emem-dev-data-availability-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Deforestation Alert API from emem — 1 operation(s) for deforestation alert.
  name: emem Deforestation Alert API
  slug: emem-dev-deforestation-alert-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Demos API from emem — 1 operation(s) for demos.
  name: emem Demos API
  slug: emem-dev-demos-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The derive API from emem — 2 operation(s) for derive.
  name: emem Derive API
  slug: emem-dev-derive-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The device API from emem — 2 operation(s) for device.
  name: emem Device API
  slug: emem-dev-device-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Device Platforms API from emem — 1 operation(s) for device platforms.
  name: emem Device Platforms API
  slug: emem-dev-device-platforms-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Diff API from emem — 1 operation(s) for diff.
  name: emem Diff API
  slug: emem-dev-diff-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Discover API from emem — 12 operation(s) for discover.
  name: emem Discover API
  slug: emem-dev-discover-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The edges API from emem — 2 operation(s) for edges.
  name: emem Edges API
  slug: emem-dev-edges-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The embedding API from emem — 2 operation(s) for embedding.
  name: emem Embedding API
  slug: emem-dev-embedding-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Embedding Centroid API from emem — 1 operation(s) for embedding centroid.
  name: emem Embedding Centroid API
  slug: emem-dev-embedding-centroid-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Embedding Diversity API from emem — 1 operation(s) for embedding diversity.
  name: emem Embedding Diversity API
  slug: emem-dev-embedding-diversity-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Enroll Attested API from emem — 1 operation(s) for enroll attested.
  name: emem Enroll Attested API
  slug: emem-dev-enroll-attested-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Enroll Verify API from emem — 1 operation(s) for enroll verify.
  name: emem Enroll Verify API
  slug: emem-dev-enroll-verify-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The entity API from emem — 4 operation(s) for entity.
  name: emem Entity API
  slug: emem-dev-entity-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Errors API from emem — 1 operation(s) for errors.
  name: emem Errors API
  slug: emem-dev-errors-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The eudr API from emem — 1 operation(s) for eudr.
  name: emem Eudr API
  slug: emem-dev-eudr-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The fetch API from emem — 2 operation(s) for fetch.
  name: emem Fetch API
  slug: emem-dev-fetch-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Field Boundaries API from emem — 1 operation(s) for field boundaries.
  name: emem Field Boundaries API
  slug: emem-dev-field-boundaries-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Find Similar API from emem — 1 operation(s) for find similar.
  name: emem Find Similar API
  slug: emem-dev-find-similar-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Fleet API from emem — 1 operation(s) for fleet.
  name: emem Fleet API
  slug: emem-dev-fleet-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Functions API from emem — 1 operation(s) for functions.
  name: emem Functions API
  slug: emem-dev-functions-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The get_fact API from emem — 1 operation(s) for get_fact.
  name: emem Get Fact API
  slug: emem-dev-get-fact-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Grid Info API from emem — 1 operation(s) for grid info.
  name: emem Grid Info API
  slug: emem-dev-grid-info-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Health API from emem — 2 operation(s) for health.
  name: emem Health API
  slug: emem-dev-health-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Heat Solve API from emem — 1 operation(s) for heat solve.
  name: emem Heat Solve API
  slug: emem-dev-heat-solve-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The hunter API from emem — 1 operation(s) for hunter.
  name: emem Hunter API
  slug: emem-dev-hunter-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The identity API from emem — 7 operation(s) for identity.
  name: emem Identity API
  slug: emem-dev-identity-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Inbox API from emem — 1 operation(s) for inbox.
  name: emem Inbox API
  slug: emem-dev-inbox-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Intent API from emem — 1 operation(s) for intent.
  name: emem Intent API
  slug: emem-dev-intent-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The introspect API from emem — 2 operation(s) for introspect.
  name: emem Introspect API
  slug: emem-dev-introspect-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Jepa Predict API from emem — 1 operation(s) for jepa predict.
  name: emem Jepa Predict API
  slug: emem-dev-jepa-predict-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Jepa Predict V2 API from emem — 1 operation(s) for jepa predict v2.
  name: emem Jepa Predict V2 API
  slug: emem-dev-jepa-predict-v2-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The knowledge-graph API from emem — 2 operation(s) for knowledge-graph.
  name: emem Knowledge Graph API
  slug: emem-dev-knowledge-graph-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Live API from emem — 1 operation(s) for live.
  name: emem Live API
  slug: emem-dev-live-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Locate API from emem — 1 operation(s) for locate.
  name: emem Locate API
  slug: emem-dev-locate-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Log API from emem — 6 operation(s) for log.
  name: emem Log API
  slug: emem-dev-log-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Manifests API from emem — 1 operation(s) for manifests.
  name: emem Manifests API
  slug: emem-dev-manifests-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Materializers API from emem — 1 operation(s) for materializers.
  name: emem Materializers API
  slug: emem-dev-materializers-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Mcp API from emem — 1 operation(s) for mcp.
  name: emem MCP API
  slug: emem-dev-mcp-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The memory API from emem — 14 operation(s) for memory.
  name: emem Memory API
  slug: emem-dev-memory-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Memory Token API from emem — 3 operation(s) for memory token.
  name: emem Memory Token API
  slug: emem-dev-memory-token-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Neighborhood Consistency API from emem — 1 operation(s) for neighborhood consistency.
  name: emem Neighborhood Consistency API
  slug: emem-dev-neighborhood-consistency-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Query Region API from emem — 1 operation(s) for query region.
  name: emem Query Region API
  slug: emem-dev-query-region-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Quickstart API from emem — 1 operation(s) for quickstart.
  name: emem Quickstart API
  slug: emem-dev-quickstart-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Raster API from emem — 1 operation(s) for raster.
  name: emem Raster API
  slug: emem-dev-raster-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Raster Bundle API from emem — 2 operation(s) for raster bundle.
  name: emem Raster Bundle API
  slug: emem-dev-raster-bundle-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The reason API from emem — 1 operation(s) for reason.
  name: emem Reason API
  slug: emem-dev-reason-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Recall API from emem — 1 operation(s) for recall.
  name: emem Recall API
  slug: emem-dev-recall-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Recall Many API from emem — 1 operation(s) for recall many.
  name: emem Recall Many API
  slug: emem-dev-recall-many-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Recall Polygon API from emem — 1 operation(s) for recall polygon.
  name: emem Recall Polygon API
  slug: emem-dev-recall-polygon-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Region Similarity API from emem — 1 operation(s) for region similarity.
  name: emem Region Similarity API
  slug: emem-dev-region-similarity-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The render API from emem — 1 operation(s) for render.
  name: emem Render API
  slug: emem-dev-render-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Reviews API from emem — 2 operation(s) for reviews.
  name: emem Reviews API
  slug: emem-dev-reviews-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Rice Ch4 API from emem — 1 operation(s) for rice ch4.
  name: emem Rice Ch4 API
  slug: emem-dev-rice-ch4-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Sar Forest Disturbance API from emem — 1 operation(s) for sar forest disturbance.
  name: emem Sar Forest Disturbance API
  slug: emem-dev-sar-forest-disturbance-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Schema API from emem — 1 operation(s) for schema.
  name: emem Schema API
  slug: emem-dev-schema-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The security API from emem — 2 operation(s) for security.
  name: emem Security API
  slug: emem-dev-security-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Sources API from emem — 1 operation(s) for sources.
  name: emem Sources API
  slug: emem-dev-sources-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Spi API from emem — 1 operation(s) for spi.
  name: emem Spi API
  slug: emem-dev-spi-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The State API from emem — 1 operation(s) for state.
  name: emem State API
  slug: emem-dev-state-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The State Diff API from emem — 1 operation(s) for state diff.
  name: emem State Diff API
  slug: emem-dev-state-diff-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The State Multi API from emem — 1 operation(s) for state multi.
  name: emem State Multi API
  slug: emem-dev-state-multi-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Stream API from emem — 1 operation(s) for stream.
  name: emem Stream API
  slug: emem-dev-stream-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Substrates API from emem — 1 operation(s) for substrates.
  name: emem Substrates API
  slug: emem-dev-substrates-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Temporal Route API from emem — 1 operation(s) for temporal route.
  name: emem Temporal Route API
  slug: emem-dev-temporal-route-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Terrain API from emem — 1 operation(s) for terrain.
  name: emem Terrain API
  slug: emem-dev-terrain-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Tools API from emem — 1 operation(s) for tools.
  name: emem Tools API
  slug: emem-dev-tools-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Topics API from emem — 1 operation(s) for topics.
  name: emem Topics API
  slug: emem-dev-topics-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Trace Encodings API from emem — 1 operation(s) for trace encodings.
  name: emem Trace Encodings API
  slug: emem-dev-trace-encodings-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Trace Resolve API from emem — 1 operation(s) for trace resolve.
  name: emem Trace Resolve API
  slug: emem-dev-trace-resolve-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Trace Verify API from emem — 1 operation(s) for trace verify.
  name: emem Trace Verify API
  slug: emem-dev-trace-verify-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Trajectory API from emem — 1 operation(s) for trajectory.
  name: emem Trajectory API
  slug: emem-dev-trajectory-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Triple Consensus API from emem — 1 operation(s) for triple consensus.
  name: emem Triple Consensus API
  slug: emem-dev-triple-consensus-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The vector API from emem — 1 operation(s) for vector.
  name: emem Vector API
  slug: emem-dev-vector-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Verify API from emem — 8 operation(s) for verify.
  name: emem Verify API
  slug: emem-dev-verify-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Verify Receipt API from emem — 1 operation(s) for verify receipt.
  name: emem Verify Receipt API
  slug: emem-dev-verify-receipt-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Wave Solve API from emem — 1 operation(s) for wave solve.
  name: emem Wave Solve API
  slug: emem-dev-wave-solve-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The .well Known API from emem — 1 operation(s) for .well known.
  name: emem .well Known API
  slug: emem-dev-well-known-api
- baseURL: https://emem.dev/mcp
  baseurl_source: declared
  description: The Worlds API from emem — 1 operation(s) for worlds.
  name: emem Worlds API
  slug: emem-dev-worlds-api
artifact_total: 135
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://emem.dev/.well-known/emem-readonly.json
- group: other
  href: https://artifacts.apis.io/emem-dev/capabilities/emem-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/emem-dev-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/emem-dev/overlays/emem-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/emem-dev-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://emem.dev/
- group: auth
  href: https://artifacts.apis.io/emem-dev/security/emem-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/emem-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/emem-dev/security/emem-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/emem-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/emem-dev/security/emem-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emem-dev-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/emem-dev/authentication/emem-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emem-dev-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vortx.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://emem.dev/reference
- group: docs
  title: ''
  type: Documentation
  url: https://emem.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://emem.dev/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://emem.dev/docs/quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://emem.dev/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vortx-AI
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Vortx-AI/emem
- group: operate
  title: ''
  type: Roadmap
  url: https://emem.dev/docs/roadmap.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emem.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emem.dev/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Vortx-AI/emem/blob/main/CHANGELOG.md
- group: operate
  href: https://artifacts.apis.io/emem-dev/changelog/emem-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/emem-dev-changelog.yml
- group: agent
  href: https://artifacts.apis.io/emem-dev/llms/emem-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emem-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/emem-dev/a2a/emem-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/emem-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/emem-dev/well-known/emem-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/emem-dev-well-known.yml
- group: auth
  href: https://artifacts.apis.io/emem-dev/well-known/emem-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/emem-dev-security.txt
- group: other
  href: https://artifacts.apis.io/emem-dev/well-known/emem-dev-oauth-authorization-server.json
  title: ''
  type: OpenIDConnect
  url: well-known/emem-dev-oauth-authorization-server.json
- group: build
  href: https://artifacts.apis.io/emem-dev/packages/emem-dev-packages.yml
  title: ''
  type: Packages
  url: packages/emem-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/emem-dev/packages/emem-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/emem-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/emem-dev/cli/emem-dev-cli.yml
  title: ''
  type: CLI
  url: cli/emem-dev-cli.yml
- group: agent
  href: https://artifacts.apis.io/emem-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/emem-dev/conformance/emem-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emem-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/emem-dev/lifecycle/emem-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/emem-dev-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/emem-dev/lifecycle/emem-dev-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/emem-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/emem-dev/conventions/emem-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/emem-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/emem-dev/conventions/emem-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/emem-dev-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/emem-dev/plans/emem-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/emem-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/emem-dev/rate-limits/emem-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/emem-dev-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/emem-dev/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/emem-dev-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/emem-dev/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/emem-dev-regulatory-posture.yml
- group: operate
  href: https://artifacts.apis.io/emem-dev/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: SupportLifetime
  url: regulatory/emem-dev-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/emem-dev/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/emem-dev-regulatory-posture.yml
created: '2026-09-19'
description: Vortx AI Private Limited is a spatial AI lab based in India that builds and operates emem (emem.dev), an Apache-2.0 protocol and hosted responder providing shared, verifiable memory for AI agents. Every place on Earth has one 64-bit address (cell64), every observation is an ed25519-signed, content-addressed fact materialised from satellite and open Earth-observation archives, and any agent can read without a key or account and verify the receipt offline. The surface is published as an OpenAPI 3.1 contract (196 operations), a remote MCP server (110 tools), an A2A 1.0 agent card, an llms.txt, RFC 8414 / RFC 9728 discovery documents, and first-party Python and TypeScript clients.
finops:
- has_sources: true
  method: derived
  name: Emem Dev Finops
  primary_unit: ''
  service_category: ''
  slug: emem-dev-finops
  template: true
image: https://emem.dev/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at emem.dev over streamable HTTP; 110 tools listed.
  name: emem MCP Server
  slug: emem
modified: '2026-09-19'
name: emem
nav: Providers
network: true
overview: 'emem publishes 115 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Agent Card API, Agent Stats API, and 112 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Memory, and Geospatial.


  The emem catalog on APIs.io includes 1 Spectral governance ruleset.


  emem''s developer surface includes pricing, authentication, documentation, API reference, getting-started guide, support, GitHub presence, and 34 more developer resources.'
plans:
- name: Emem Dev Plans Pricing
  plan_count: 1
  slug: emem-dev-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Emem Dev Rate Limits
  slug: emem-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: emem API Rules
  rule_count: 52
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 14
  slug: emem-dev-rules
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 47.1
    developer_ergonomics: 54.8
    discoverability: 75.0
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 60.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 113
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/emem-dev/emem-dev-2026-10-11T104144.png
security:
- kind: authentication
  name: Emem Dev Authentication
  slug: emem-dev-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Emem Dev Domain Security
  slug: emem-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Emem Dev Vulnerability Disclosure
  slug: emem-dev-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 12
skills:
- name: emem-a2a-collaboration
  slug: emem-dev-a2a-collaboration
- name: emem-agent-handoff
  slug: emem-dev-agent-handoff
- name: emem-field-tokens
  slug: emem-dev-field-tokens
- name: emem-find-similar
  slug: emem-dev-find-similar
- name: emem-locate-and-recall
  slug: emem-dev-locate-and-recall
- name: emem-recall-polygon
  slug: emem-dev-recall-polygon
- name: emem-referential-drift
  slug: emem-dev-referential-drift
- name: selfhost-emem-guard
  slug: emem-dev-selfhost-emem-guard
- name: emem-shared-identity
  slug: emem-dev-shared-identity
- name: emem-sign-and-attest
  slug: emem-dev-sign-and-attest
- name: emem-verify-before-publish
  slug: emem-dev-verify-before-publish
- name: emem-verify-receipt
  slug: emem-dev-verify-receipt
slug: emem-dev
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Memory
- Geospatial
- Earth Observation
- Satellite Imagery
- Provenance
- Cryptography
- MCP
- Open Source
- India
- A2A
website: https://emem.dev/
---
