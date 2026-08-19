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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Reactome Agentic Access
  operation_count: 122
  slug: reactome-agentic-access
  summary_line: 122 operations · 31 acting
api_count: 23
apis:
- description: Database info queries
  name: Reactome database API
  slug: reactome-database-api
- description: 'Reactome Data: Search engines discovery schema'
  name: Reactome discover API
  slug: reactome-discover-api
- description: 'Reactome Data: Disease related queries'
  name: Reactome diseases API
  slug: reactome-diseases-api
- description: Methods to download different views of a result
  name: Reactome download API
  slug: reactome-download-api
- description: 'Reactome Data: PhysicalEntity queries'
  name: Reactome entities API
  slug: reactome-entities-api
- description: 'Reactome Data: Queries related to events'
  name: Reactome events API
  slug: reactome-events-api
- description: 'Reactome Data: Format Exporter'
  name: Reactome exporter API
  slug: reactome-exporter-api
- description: Queries for only one identifier
  name: Reactome identifier API
  slug: reactome-identifier-api
- description: Queries for multiple identifiers
  name: Reactome identifiers API
  slug: reactome-identifiers-api
- description: Imports an external result
  name: Reactome import API
  slug: reactome-import-api
- description: Molecule interactors
  name: Reactome interactors API
  slug: reactome-interactors-api
- description: Identifiers mapping methods
  name: Reactome mapping API
  slug: reactome-mapping-api
- description: 'Reactome Data: Orthology related queries'
  name: Reactome orthology API
  slug: reactome-orthology-api
- description: 'Reactome Data: Queries related to participants'
  name: Reactome participants API
  slug: reactome-participants-api
- description: 'Reactome Data: Pathway related queries'
  name: Reactome pathways API
  slug: reactome-pathways-api
- description: 'Reactome Data: Person queries'
  name: Reactome person API
  slug: reactome-person-api
- description: 'Reactome Data: Common data retrieval'
  name: Reactome query API
  slug: reactome-query-api
- description: 'Reactome xRefs: ReferenceEntity queries'
  name: Reactome references API
  slug: reactome-references-api
- description: Retrieves report files in PDF format
  name: Reactome report API
  slug: reactome-report-api
- description: 'Reactome Data: Schema class queries'
  name: Reactome schema API
  slug: reactome-schema-api
- description: Reactome Search
  name: Reactome search API
  slug: reactome-search-api
- description: Species comparison
  name: Reactome species API
  slug: reactome-species-api
- description: Previous queries filter
  name: Reactome token API
  slug: reactome-token-api
artifact_total: 122
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pathway Analysis Service database API
  slug: open-reactome-database-api
- collection_type: open
  name: Pathway Analysis Service database discover API
  slug: open-reactome-discover-api
- collection_type: open
  name: Pathway Analysis Service database diseases API
  slug: open-reactome-diseases-api
- collection_type: open
  name: Pathway Analysis Service database download API
  slug: open-reactome-download-api
- collection_type: open
  name: Pathway Analysis Service database entities API
  slug: open-reactome-entities-api
- collection_type: open
  name: Pathway Analysis Service database events API
  slug: open-reactome-events-api
- collection_type: open
  name: Pathway Analysis Service database exporter API
  slug: open-reactome-exporter-api
- collection_type: open
  name: Pathway Analysis Service database identifier API
  slug: open-reactome-identifier-api
- collection_type: open
  name: Pathway Analysis Service database identifiers API
  slug: open-reactome-identifiers-api
- collection_type: open
  name: Pathway Analysis Service database import API
  slug: open-reactome-import-api
- collection_type: open
  name: Pathway Analysis Service database interactors API
  slug: open-reactome-interactors-api
- collection_type: open
  name: Pathway Analysis Service database mapping API
  slug: open-reactome-mapping-api
- collection_type: open
  name: Pathway Analysis Service database orthology API
  slug: open-reactome-orthology-api
- collection_type: open
  name: Pathway Analysis Service database participants API
  slug: open-reactome-participants-api
- collection_type: open
  name: Pathway Analysis Service database pathways API
  slug: open-reactome-pathways-api
- collection_type: open
  name: Pathway Analysis Service database person API
  slug: open-reactome-person-api
- collection_type: open
  name: Pathway Analysis Service database query API
  slug: open-reactome-query-api
- collection_type: open
  name: Pathway Analysis Service database references API
  slug: open-reactome-references-api
- collection_type: open
  name: Pathway Analysis Service database report API
  slug: open-reactome-report-api
- collection_type: open
  name: Pathway Analysis Service database schema API
  slug: open-reactome-schema-api
- collection_type: open
  name: Pathway Analysis Service database search API
  slug: open-reactome-search-api
- collection_type: open
  name: Pathway Analysis Service database species API
  slug: open-reactome-species-api
- collection_type: open
  name: Pathway Analysis Service database token API
  slug: open-reactome-token-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reactome-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reactome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reactome.org/
- group: docs
  title: ''
  type: Documentation
  url: https://reactome.org/documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://reactome.org/dev
- group: design
  title: ''
  type: DataModel
  url: https://reactome.org/documentation/data-model
- group: operate
  title: ''
  type: FAQ
  url: https://reactome.org/documentation/faq
- group: build
  title: ''
  type: GitHub
  url: https://github.com/reactome
- group: company
  title: ''
  type: Blog
  url: https://reactome.org/about/news
- group: commercial
  title: ''
  type: License
  url: https://reactome.org/license
- group: operate
  title: ''
  type: Contact
  url: https://reactome.org/about/contact-us
- group: company
  title: ''
  type: About
  url: https://reactome.org/about
created: '2026-06-13'
description: Reactome is a free, open-source, curated, and peer-reviewed biological pathway database. It provides comprehensive pathway data covering human biology and orthologous reactions for over 14 non-human species including mouse, rat, yeast, and fruit fly. The platform exposes two primary REST APIs — the Content Service for querying pathway data, molecular interactions, species comparisons, and reaction network visualization, and the Analysis Service for pathway enrichment analysis of gene and protein identifier lists. Both APIs are freely accessible without authentication, fully documented with OpenAPI (Swagger), and cross-referenced with major biological databases including NCBI, Ensembl, UniProt, KEGG, ChEBI, PubMed, and Gene Ontology. Data is authored by expert biologist researchers and maintained by Reactome editorial staff.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reactome.png
json_schemas:
- name: AnalysisResult
  property_count: 8
  slug: analysis-service-analysisresult
- name: AnalysisSummary
  property_count: 11
  slug: analysis-service-analysissummary
- name: Bin
  property_count: 2
  slug: analysis-service-bin
- name: EntityStatistics
  property_count: 11
  slug: analysis-service-entitystatistics
- name: ExpressionSummary
  property_count: 3
  slug: analysis-service-expressionsummary
- name: ExternalAnalysisReaction
  property_count: 3
  slug: analysis-service-externalanalysisreaction
- name: ExternalAnalysisResult
  property_count: 5
  slug: analysis-service-externalanalysisresult
- name: ExternalAnalysisSummary
  property_count: 10
  slug: analysis-service-externalanalysissummary
- name: ExternalExpressionSummary
  property_count: 3
  slug: analysis-service-externalexpressionsummary
- name: ExternalIdentifier
  property_count: 3
  slug: analysis-service-externalidentifier
- name: ExternalInteraction
  property_count: 2
  slug: analysis-service-externalinteraction
- name: ExternalInteractor
  property_count: 3
  slug: analysis-service-externalinteractor
- name: ExternalMainIdentifier
  property_count: 2
  slug: analysis-service-externalmainidentifier
- name: ExternalPathwayNodeData
  property_count: 4
  slug: analysis-service-externalpathwaynodedata
- name: ExternalPathwayNodeSummary
  property_count: 7
  slug: analysis-service-externalpathwaynodesummary
- name: ExternalSpeciesNode
  property_count: 3
  slug: analysis-service-externalspeciesnode
- name: ExternalStatistics
  property_count: 15
  slug: analysis-service-externalstatistics
- name: FoundElements
  property_count: 7
  slug: analysis-service-foundelements
- name: FoundEntities
  property_count: 6
  slug: analysis-service-foundentities
- name: FoundEntity
  property_count: 3
  slug: analysis-service-foundentity
- name: FoundInteractor
  property_count: 4
  slug: analysis-service-foundinteractor
- name: FoundInteractors
  property_count: 4
  slug: analysis-service-foundinteractors
- name: IdentifierMap
  property_count: 2
  slug: analysis-service-identifiermap
- name: IdentifierSummary
  property_count: 2
  slug: analysis-service-identifiersummary
- name: MappedEntity
  property_count: 2
  slug: analysis-service-mappedentity
- name: MappedIdentifier
  property_count: 3
  slug: analysis-service-mappedidentifier
- name: PathwayBase
  property_count: 4
  slug: analysis-service-pathwaybase
- name: PathwaySummary
  property_count: 8
  slug: analysis-service-pathwaysummary
- name: ReactionStatistics
  property_count: 4
  slug: analysis-service-reactionstatistics
- name: ResourceSummary
  property_count: 3
  slug: analysis-service-resourcesummary
- name: SpeciesFilteredResult
  property_count: 3
  slug: analysis-service-speciesfilteredresult
- name: SpeciesSummary
  property_count: 5
  slug: analysis-service-speciessummary
- name: ComponentOf
  property_count: 5
  slug: content-service-componentof
- name: CrossReferenceResult
  property_count: 3
  slug: content-service-crossreferenceresult
- name: CustomInteraction
  property_count: 12
  slug: content-service-custominteraction
- name: CustomPsicquicResource
  property_count: 1
  slug: content-service-custompsicquicresource
- name: DatabaseObject
  property_count: 8
  slug: content-service-databaseobject
- name: DiagramOccurrencesResult
  property_count: 4
  slug: content-service-diagramoccurrencesresult
- name: DiagramResult
  property_count: 3
  slug: content-service-diagramresult
- name: Entry
  property_count: 47
  slug: content-service-entry
- name: EventProjection
  property_count: 20
  slug: content-service-eventprojection
- name: FacetContainer
  property_count: 2
  slug: content-service-facetcontainer
- name: FacetList
  property_count: 2
  slug: content-service-facetlist
- name: FacetMapping
  property_count: 6
  slug: content-service-facetmapping
- name: FireworksOccurrencesResult
  property_count: 2
  slug: content-service-fireworksoccurrencesresult
- name: FireworksResult
  property_count: 4
  slug: content-service-fireworksresult
- name: GroupedResult
  property_count: 5
  slug: content-service-groupedresult
- name: IconPhysicalEntity
  property_count: 5
  slug: content-service-iconphysicalentity
- name: Interactor
  property_count: 7
  slug: content-service-interactor
- name: InteractorEntity
  property_count: 3
  slug: content-service-interactorentity
- name: Interactors
  property_count: 2
  slug: content-service-interactors
- name: PageableObject
  property_count: 6
  slug: content-service-pageableobject
- name: PageMapStringCollectionCrossReferenceResult
  property_count: 11
  slug: content-service-pagemapstringcollectioncrossreferenceresult
- name: Participant
  property_count: 4
  slug: content-service-participant
- name: ParticipantRefEntities
  property_count: 7
  slug: content-service-participantrefentities
- name: PathwayBrowserNode
  property_count: 7
  slug: content-service-pathwaybrowsernode
- name: PsicquicResource
  property_count: 4
  slug: content-service-psicquicresource
- name: Result
  property_count: 4
  slug: content-service-result
- name: SchemaCreator
  property_count: 0
  slug: content-service-schemacreator
- name: SchemaDataCatalog
  property_count: 3
  slug: content-service-schemadatacatalog
- name: SchemaDataDownload
  property_count: 4
  slug: content-service-schemadatadownload
- name: SchemaDataSet
  property_count: 13
  slug: content-service-schemadataset
- name: SchemaNode
  property_count: 3
  slug: content-service-schemanode
- name: ShortCrossReference
  property_count: 3
  slug: content-service-shortcrossreference
- name: SimpleDatabaseObject
  property_count: 5
  slug: content-service-simpledatabaseobject
- name: SimpleEventProjection
  property_count: 9
  slug: content-service-simpleeventprojection
- name: SimpleReferenceObject
  property_count: 3
  slug: content-service-simplereferenceobject
- name: Sort
  property_count: 3
  slug: content-service-sort
- name: Summary
  property_count: 5
  slug: content-service-summary
- name: TargetResult
  property_count: 3
  slug: content-service-targetresult
- name: TupleResult
  property_count: 2
  slug: content-service-tupleresult
jsonld:
- class_count: 0
  name: Reactome Context
  property_count: 94
  slug: reactome-context
layout: provider
modified: '2026-06-13'
name: Reactome
nav: Providers
network: true
overview: 'Reactome publishes 23 APIs on the [APIs.io](https://apis.io/) network, including database API, discover API, diseases API, and 20 more. Tagged areas include Biological Pathways, Bioinformatics, Life Sciences, Pathway Analysis, and Gene Enrichment.


  The Reactome catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Reactome''s developer surface includes documentation, FAQ, GitHub presence, engineering blog, and 8 more developer resources.'
random_paper: 103
rules:
- effective_rule_count: 5
  extends: []
  name: Reactome API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: reactome-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.9
  delta: -4.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 52.5
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 30.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reactome/refs/heads/main/screenshots/reactome-2026-06-20T192632.png
security:
- kind: domain-security
  name: Reactome Domain Security
  slug: reactome-domain-security
  summary_line: TLSv1.3 · DMARC
slug: reactome
tags:
- Biological Pathways
- Bioinformatics
- Life Sciences
- Pathway Analysis
- Gene Enrichment
- Molecular Interactions
- Systems Biology
- Open Science
website: https://reactome.org/
---
