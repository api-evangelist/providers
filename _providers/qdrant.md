---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Qdrant Agentic Access
  operation_count: 73
  slug: qdrant-agentic-access
  summary_line: 73 operations · 48 acting
api_count: 9
apis:
- description: Additional names for existing collections.
  name: Qdrant Aliases API
  slug: qdrant-aliases-api
- description: Beta features, do not depend on these yet.
  name: Qdrant Beta API
  slug: qdrant-beta-api
- description: Searchable collections of points.
  name: Qdrant Collections API
  slug: qdrant-collections-api
- description: Service distributed setup.
  name: Qdrant Distributed API
  slug: qdrant-distributed-api
- description: Indexes for payloads associated with points.
  name: Qdrant Indexes API
  slug: qdrant-indexes-api
- description: Float-point vectors with payload.
  name: Qdrant Points API
  slug: qdrant-points-api
- description: Find points in a collection.
  name: Qdrant Search API
  slug: qdrant-search-api
- description: Qdrant service utilities.
  name: Qdrant Service API
  slug: qdrant-service-api
- description: Storage and collections snapshots.
  name: Qdrant Snapshots API
  slug: qdrant-snapshots-api
artifact_total: 431
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qdrant Aliases API
  slug: open-qdrant-aliases-api
- collection_type: open
  name: Qdrant Aliases Beta API
  slug: open-qdrant-beta-api
- collection_type: open
  name: Qdrant Aliases Collections API
  slug: open-qdrant-collections-api
- collection_type: open
  name: Qdrant Aliases Distributed API
  slug: open-qdrant-distributed-api
- collection_type: open
  name: Qdrant Aliases Indexes API
  slug: open-qdrant-indexes-api
- collection_type: open
  name: Qdrant API
  slug: open-qdrant-openapi-original
- collection_type: open
  name: Qdrant Aliases Points API
  slug: open-qdrant-points-api
- collection_type: open
  name: Qdrant Aliases Search API
  slug: open-qdrant-search-api
- collection_type: open
  name: Qdrant Aliases Service API
  slug: open-qdrant-service-api
- collection_type: open
  name: Qdrant Aliases Snapshots API
  slug: open-qdrant-snapshots-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qdrant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qdrant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qdrant-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qdrant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qdrant
- group: start
  title: ''
  type: GettingStarted
  url: https://qdrant.tech/documentation/quick-start/
- group: docs
  title: ''
  type: Documentation
  url: https://qdrant.tech/documentation/concepts/
- group: learn
  title: ''
  type: Tutorials
  url: https://qdrant.tech/documentation/tutorials/
- group: commercial
  title: ''
  type: Pricing
  url: https://qdrant.tech/pricing/
- group: company
  title: ''
  type: Blog
  url: https://qdrant.tech/blog/
- group: company
  title: ''
  type: Website
  url: https://qdrant.tech
- group: agent
  title: ''
  type: LlmsText
  url: https://qdrant.tech/llms.txt
created: '2024-06-18'
description: Qdrant is a vector similarity search engine that provides a production-ready service with a convenient API to store, search, and manage points (i.e. vectors) with an additional payload. You can think of the payloads as additional pieces of information that can help you hone in on your search and also receive useful information that you can give to your users.
features:
- 'Free Tier: single-node 0.5 vCPU / 1 GB RAM / 4 GB disk'
- 'Standard: usage-based dedicated resources, 99.5% SLA'
- 'Premium: SSO, private VPC, 99.9% SLA'
- 'Hybrid Cloud: runs on your infra, managed via Qdrant Cloud'
- 'Private Cloud: dedicated isolated deployment'
- REST and gRPC APIs
- Throughput scales with cluster resources
- Batch upsert up to 10,000 points/request
- Sparse vectors and hybrid search
- Quantization (scalar, binary, product)
- Snapshot backup / restore
- Multi-tenancy via collections + payload filtering
- Distributed deployment with sharding
- Web UI for collection management
- Cloud Inference for embeddings (selected models free)
- Open-source self-hosted alternative
finops:
- name: Qdrant Finops
  service_category: Vector Database
  slug: qdrant-finops
graphqls:
- description: Qdrant is an open-source vector database and similarity search engine. The API covers collection management, point upsert and search, payload filtering, vector quantization, snapshots, and cluster man
  name: Qdrant GraphQL API
  slug: qdrant-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qdrant.png
json_schemas:
- name: AbortResharding
  property_count: 0
  slug: qdrant-abortresharding
- name: AbortReshardingOperation
  property_count: 1
  slug: qdrant-abortreshardingoperation
- name: AbortShardTransfer
  property_count: 3
  slug: qdrant-abortshardtransfer
- name: AbortTransferOperation
  property_count: 1
  slug: qdrant-aborttransferoperation
- name: AbsExpression
  property_count: 1
  slug: qdrant-absexpression
- name: AcornSearchParams
  property_count: 2
  slug: qdrant-acornsearchparams
- name: AliasDescription
  property_count: 2
  slug: qdrant-aliasdescription
- name: AliasOperations
  property_count: 0
  slug: qdrant-aliasoperations
- name: AnyVariants
  property_count: 0
  slug: qdrant-anyvariants
- name: AppBuildTelemetry
  property_count: 9
  slug: qdrant-appbuildtelemetry
- name: AppFeaturesTelemetry
  property_count: 6
  slug: qdrant-appfeaturestelemetry
- name: Batch
  property_count: 3
  slug: qdrant-batch
- name: BatchVectorStruct
  property_count: 0
  slug: qdrant-batchvectorstruct
- name: BinaryQuantization
  property_count: 1
  slug: qdrant-binaryquantization
- name: BinaryQuantizationConfig
  property_count: 3
  slug: qdrant-binaryquantizationconfig
- name: BinaryQuantizationEncoding
  property_count: 0
  slug: qdrant-binaryquantizationencoding
- name: BinaryQuantizationQueryEncoding
  property_count: 0
  slug: qdrant-binaryquantizationqueryencoding
- name: Bm25Config
  property_count: 11
  slug: qdrant-bm25config
- name: BoolIndexParams
  property_count: 3
  slug: qdrant-boolindexparams
- name: BoolIndexType
  property_count: 0
  slug: qdrant-boolindextype
- name: ChangeAliasesOperation
  property_count: 1
  slug: qdrant-changealiasesoperation
- name: ClearPayloadOperation
  property_count: 1
  slug: qdrant-clearpayloadoperation
- name: ClusterConfigTelemetry
  property_count: 3
  slug: qdrant-clusterconfigtelemetry
- name: ClusterOperations
  property_count: 0
  slug: qdrant-clusteroperations
- name: ClusterStatus
  property_count: 0
  slug: qdrant-clusterstatus
- name: ClusterStatusTelemetry
  property_count: 8
  slug: qdrant-clusterstatustelemetry
- name: ClusterTelemetry
  property_count: 7
  slug: qdrant-clustertelemetry
- name: CollectionClusterInfo
  property_count: 6
  slug: qdrant-collectionclusterinfo
- name: CollectionConfig
  property_count: 7
  slug: qdrant-collectionconfig
- name: CollectionConfigTelemetry
  property_count: 8
  slug: qdrant-collectionconfigtelemetry
- name: CollectionDescription
  property_count: 1
  slug: qdrant-collectiondescription
- name: CollectionExistence
  property_count: 1
  slug: qdrant-collectionexistence
- name: CollectionInfo
  property_count: 9
  slug: qdrant-collectioninfo
- name: CollectionParams
  property_count: 9
  slug: qdrant-collectionparams
- name: CollectionParamsDiff
  property_count: 5
  slug: qdrant-collectionparamsdiff
- name: CollectionsAggregatedTelemetry
  property_count: 3
  slug: qdrant-collectionsaggregatedtelemetry
- name: CollectionsAliasesResponse
  property_count: 1
  slug: qdrant-collectionsaliasesresponse
- name: CollectionSnapshotTelemetry
  property_count: 4
  slug: qdrant-collectionsnapshottelemetry
- name: CollectionsResponse
  property_count: 1
  slug: qdrant-collectionsresponse
- name: CollectionStatus
  property_count: 0
  slug: qdrant-collectionstatus
- name: CollectionsTelemetry
  property_count: 4
  slug: qdrant-collectionstelemetry
- name: CollectionTelemetry
  property_count: 7
  slug: qdrant-collectiontelemetry
- name: CollectionTelemetryEnum
  property_count: 0
  slug: qdrant-collectiontelemetryenum
- name: CollectionWarning
  property_count: 1
  slug: qdrant-collectionwarning
- name: CompressionRatio
  property_count: 0
  slug: qdrant-compressionratio
- name: Condition
  property_count: 0
  slug: qdrant-condition
- name: ConsensusConfigTelemetry
  property_count: 3
  slug: qdrant-consensusconfigtelemetry
- name: ConsensusThreadStatus
  property_count: 0
  slug: qdrant-consensusthreadstatus
- name: ContextExamplePair
  property_count: 2
  slug: qdrant-contextexamplepair
- name: ContextInput
  property_count: 0
  slug: qdrant-contextinput
- name: ContextPair
  property_count: 2
  slug: qdrant-contextpair
- name: ContextQuery
  property_count: 1
  slug: qdrant-contextquery
- name: CountRequest
  property_count: 3
  slug: qdrant-countrequest
- name: CountResult
  property_count: 1
  slug: qdrant-countresult
- name: CpuEndian
  property_count: 0
  slug: qdrant-cpuendian
- name: CreateAlias
  property_count: 2
  slug: qdrant-createalias
- name: CreateAliasOperation
  property_count: 1
  slug: qdrant-createaliasoperation
- name: CreateCollection
  property_count: 13
  slug: qdrant-createcollection
- name: CreateFieldIndex
  property_count: 2
  slug: qdrant-createfieldindex
- name: CreateShardingKey
  property_count: 5
  slug: qdrant-createshardingkey
- name: CreateShardingKeyOperation
  property_count: 1
  slug: qdrant-createshardingkeyoperation
- name: Datatype
  property_count: 0
  slug: qdrant-datatype
- name: DatetimeExpression
  property_count: 1
  slug: qdrant-datetimeexpression
- name: DatetimeIndexParams
  property_count: 4
  slug: qdrant-datetimeindexparams
- name: DatetimeIndexType
  property_count: 0
  slug: qdrant-datetimeindextype
- name: DatetimeKeyExpression
  property_count: 1
  slug: qdrant-datetimekeyexpression
- name: DatetimeRange
  property_count: 4
  slug: qdrant-datetimerange
- name: DecayParamsExpression
  property_count: 4
  slug: qdrant-decayparamsexpression
- name: DeleteAlias
  property_count: 1
  slug: qdrant-deletealias
- name: DeleteAliasOperation
  property_count: 1
  slug: qdrant-deletealiasoperation
- name: DeleteOperation
  property_count: 1
  slug: qdrant-deleteoperation
- name: DeletePayload
  property_count: 4
  slug: qdrant-deletepayload
- name: DeletePayloadOperation
  property_count: 1
  slug: qdrant-deletepayloadoperation
- name: DeleteVectors
  property_count: 4
  slug: qdrant-deletevectors
- name: DeleteVectorsOperation
  property_count: 1
  slug: qdrant-deletevectorsoperation
- name: Direction
  property_count: 0
  slug: qdrant-direction
- name: Disabled
  property_count: 0
  slug: qdrant-disabled
- name: DiscoverInput
  property_count: 2
  slug: qdrant-discoverinput
- name: DiscoverQuery
  property_count: 1
  slug: qdrant-discoverquery
- name: DiscoverRequest
  property_count: 11
  slug: qdrant-discoverrequest
- name: DiscoverRequestBatch
  property_count: 1
  slug: qdrant-discoverrequestbatch
- name: Distance
  property_count: 0
  slug: qdrant-distance
- name: DistributedClusterTelemetry
  property_count: 3
  slug: qdrant-distributedclustertelemetry
- name: DistributedCollectionTelemetry
  property_count: 4
  slug: qdrant-distributedcollectiontelemetry
- name: DistributedPeerDetails
  property_count: 7
  slug: qdrant-distributedpeerdetails
- name: DistributedPeerInfo
  property_count: 3
  slug: qdrant-distributedpeerinfo
- name: DistributedReplicaTelemetry
  property_count: 11
  slug: qdrant-distributedreplicatelemetry
- name: DistributedShardTelemetry
  property_count: 3
  slug: qdrant-distributedshardtelemetry
- name: DistributedTelemetryData
  property_count: 2
  slug: qdrant-distributedtelemetrydata
- name: DivExpression
  property_count: 1
  slug: qdrant-divexpression
- name: DivParams
  property_count: 3
  slug: qdrant-divparams
- name: Document
  property_count: 3
  slug: qdrant-document
- name: DocumentOptions
  property_count: 0
  slug: qdrant-documentoptions
- name: DropReplicaOperation
  property_count: 1
  slug: qdrant-dropreplicaoperation
- name: DropShardingKey
  property_count: 1
  slug: qdrant-dropshardingkey
- name: DropShardingKeyOperation
  property_count: 1
  slug: qdrant-dropshardingkeyoperation
- name: ErrorResponse
  property_count: 3
  slug: qdrant-errorresponse
- name: ExpDecayExpression
  property_count: 1
  slug: qdrant-expdecayexpression
- name: ExpExpression
  property_count: 1
  slug: qdrant-expexpression
- name: Expression
  property_count: 0
  slug: qdrant-expression
- name: ExtendedPointId
  property_count: 0
  slug: qdrant-extendedpointid
- name: FacetRequest
  property_count: 5
  slug: qdrant-facetrequest
- name: FacetResponse
  property_count: 1
  slug: qdrant-facetresponse
- name: FacetValue
  property_count: 0
  slug: qdrant-facetvalue
- name: FacetValueHit
  property_count: 2
  slug: qdrant-facetvaluehit
- name: FeatureFlags
  property_count: 11
  slug: qdrant-featureflags
- name: FeedbackItem
  property_count: 2
  slug: qdrant-feedbackitem
- name: FeedbackStrategy
  property_count: 0
  slug: qdrant-feedbackstrategy
- name: FieldCondition
  property_count: 9
  slug: qdrant-fieldcondition
- name: Filter
  property_count: 4
  slug: qdrant-filter
- name: FilterSelector
  property_count: 2
  slug: qdrant-filterselector
- name: FloatIndexParams
  property_count: 4
  slug: qdrant-floatindexparams
- name: FloatIndexType
  property_count: 0
  slug: qdrant-floatindextype
- name: FormulaQuery
  property_count: 2
  slug: qdrant-formulaquery
- name: Fusion
  property_count: 0
  slug: qdrant-fusion
- name: FusionQuery
  property_count: 1
  slug: qdrant-fusionquery
- name: GaussDecayExpression
  property_count: 1
  slug: qdrant-gaussdecayexpression
- name: GeoBoundingBox
  property_count: 2
  slug: qdrant-geoboundingbox
- name: GeoDistance
  property_count: 1
  slug: qdrant-geodistance
- name: GeoDistanceParams
  property_count: 2
  slug: qdrant-geodistanceparams
- name: GeoIndexParams
  property_count: 3
  slug: qdrant-geoindexparams
- name: GeoIndexType
  property_count: 0
  slug: qdrant-geoindextype
- name: GeoLineString
  property_count: 1
  slug: qdrant-geolinestring
- name: GeoPoint
  property_count: 2
  slug: qdrant-geopoint
- name: GeoPolygon
  property_count: 2
  slug: qdrant-geopolygon
- name: GeoRadius
  property_count: 2
  slug: qdrant-georadius
- name: GpuDeviceTelemetry
  property_count: 1
  slug: qdrant-gpudevicetelemetry
- name: GroupId
  property_count: 0
  slug: qdrant-groupid
- name: GroupsResult
  property_count: 1
  slug: qdrant-groupsresult
- name: GrpcTelemetry
  property_count: 2
  slug: qdrant-grpctelemetry
- name: HardwareTelemetry
  property_count: 1
  slug: qdrant-hardwaretelemetry
- name: HardwareUsage
  property_count: 7
  slug: qdrant-hardwareusage
- name: HasIdCondition
  property_count: 1
  slug: qdrant-hasidcondition
- name: HasVectorCondition
  property_count: 1
  slug: qdrant-hasvectorcondition
- name: HnswConfig
  property_count: 7
  slug: qdrant-hnswconfig
- name: HnswConfigDiff
  property_count: 7
  slug: qdrant-hnswconfigdiff
- name: HnswGlobalConfig
  property_count: 1
  slug: qdrant-hnswglobalconfig
- name: Image
  property_count: 3
  slug: qdrant-image
- name: Indexes
  property_count: 0
  slug: qdrant-indexes
- name: InferenceObject
  property_count: 3
  slug: qdrant-inferenceobject
- name: InferenceUsage
  property_count: 1
  slug: qdrant-inferenceusage
- name: IntegerIndexParams
  property_count: 6
  slug: qdrant-integerindexparams
- name: IntegerIndexType
  property_count: 0
  slug: qdrant-integerindextype
- name: IsEmptyCondition
  property_count: 1
  slug: qdrant-isemptycondition
- name: IsNullCondition
  property_count: 1
  slug: qdrant-isnullcondition
- name: KeywordIndexParams
  property_count: 4
  slug: qdrant-keywordindexparams
- name: KeywordIndexType
  property_count: 0
  slug: qdrant-keywordindextype
- name: Language
  property_count: 0
  slug: qdrant-language
- name: LinDecayExpression
  property_count: 1
  slug: qdrant-lindecayexpression
- name: LnExpression
  property_count: 1
  slug: qdrant-lnexpression
- name: LocalShardInfo
  property_count: 4
  slug: qdrant-localshardinfo
- name: LocalShardTelemetry
  property_count: 13
  slug: qdrant-localshardtelemetry
- name: Log10Expression
  property_count: 1
  slug: qdrant-log10expression
- name: LookupLocation
  property_count: 3
  slug: qdrant-lookuplocation
- name: Match
  property_count: 0
  slug: qdrant-match
- name: MatchAny
  property_count: 1
  slug: qdrant-matchany
- name: MatchExcept
  property_count: 1
  slug: qdrant-matchexcept
- name: MatchPhrase
  property_count: 1
  slug: qdrant-matchphrase
- name: MatchText
  property_count: 1
  slug: qdrant-matchtext
- name: MatchTextAny
  property_count: 1
  slug: qdrant-matchtextany
- name: MatchValue
  property_count: 1
  slug: qdrant-matchvalue
- name: MaxOptimizationThreads
  property_count: 0
  slug: qdrant-maxoptimizationthreads
- name: MaxOptimizationThreadsSetting
  property_count: 0
  slug: qdrant-maxoptimizationthreadssetting
- name: MemoryTelemetry
  property_count: 5
  slug: qdrant-memorytelemetry
- name: MessageSendErrors
  property_count: 3
  slug: qdrant-messagesenderrors
- name: MinShould
  property_count: 2
  slug: qdrant-minshould
- name: Mmr
  property_count: 2
  slug: qdrant-mmr
- name: ModelUsage
  property_count: 1
  slug: qdrant-modelusage
- name: Modifier
  property_count: 0
  slug: qdrant-modifier
- name: MoveShard
  property_count: 4
  slug: qdrant-moveshard
- name: MoveShardOperation
  property_count: 1
  slug: qdrant-moveshardoperation
- name: MultExpression
  property_count: 1
  slug: qdrant-multexpression
- name: MultiVectorComparator
  property_count: 0
  slug: qdrant-multivectorcomparator
- name: MultiVectorConfig
  property_count: 1
  slug: qdrant-multivectorconfig
- name: NaiveFeedbackStrategy
  property_count: 1
  slug: qdrant-naivefeedbackstrategy
- name: NaiveFeedbackStrategyParams
  property_count: 3
  slug: qdrant-naivefeedbackstrategyparams
- name: NamedSparseVector
  property_count: 2
  slug: qdrant-namedsparsevector
- name: NamedVector
  property_count: 2
  slug: qdrant-namedvector
- name: NamedVectorStruct
  property_count: 0
  slug: qdrant-namedvectorstruct
- name: NearestQuery
  property_count: 2
  slug: qdrant-nearestquery
- name: NegExpression
  property_count: 1
  slug: qdrant-negexpression
- name: Nested
  property_count: 2
  slug: qdrant-nested
- name: NestedCondition
  property_count: 1
  slug: qdrant-nestedcondition
- name: OperationDurationStatistics
  property_count: 7
  slug: qdrant-operationdurationstatistics
- name: Optimization
  property_count: 5
  slug: qdrant-optimization
- name: OptimizationSegmentInfo
  property_count: 2
  slug: qdrant-optimizationsegmentinfo
- name: OptimizationsResponse
  property_count: 5
  slug: qdrant-optimizationsresponse
- name: OptimizationsSummary
  property_count: 4
  slug: qdrant-optimizationssummary
- name: OptimizersConfig
  property_count: 9
  slug: qdrant-optimizersconfig
- name: OptimizersConfigDiff
  property_count: 9
  slug: qdrant-optimizersconfigdiff
- name: OptimizersStatus
  property_count: 0
  slug: qdrant-optimizersstatus
- name: OptimizerTelemetry
  property_count: 3
  slug: qdrant-optimizertelemetry
- name: OrderBy
  property_count: 3
  slug: qdrant-orderby
- name: OrderByInterface
  property_count: 0
  slug: qdrant-orderbyinterface
- name: OrderByQuery
  property_count: 1
  slug: qdrant-orderbyquery
- name: OrderValue
  property_count: 0
  slug: qdrant-ordervalue
- name: OverwritePayloadOperation
  property_count: 1
  slug: qdrant-overwritepayloadoperation
- name: P2pConfigTelemetry
  property_count: 1
  slug: qdrant-p2pconfigtelemetry
- name: PartialSnapshotTelemetry
  property_count: 3
  slug: qdrant-partialsnapshottelemetry
- name: Payload
  property_count: 0
  slug: qdrant-payload
- name: PayloadField
  property_count: 1
  slug: qdrant-payloadfield
- name: PayloadFieldSchema
  property_count: 0
  slug: qdrant-payloadfieldschema
- name: PayloadIndexInfo
  property_count: 3
  slug: qdrant-payloadindexinfo
- name: PayloadIndexTelemetry
  property_count: 5
  slug: qdrant-payloadindextelemetry
- name: PayloadSchemaParams
  property_count: 0
  slug: qdrant-payloadschemaparams
- name: PayloadSchemaType
  property_count: 0
  slug: qdrant-payloadschematype
- name: PayloadSelector
  property_count: 0
  slug: qdrant-payloadselector
- name: PayloadSelectorExclude
  property_count: 1
  slug: qdrant-payloadselectorexclude
- name: PayloadSelectorInclude
  property_count: 1
  slug: qdrant-payloadselectorinclude
- name: PayloadStorageType
  property_count: 0
  slug: qdrant-payloadstoragetype
- name: PeerInfo
  property_count: 1
  slug: qdrant-peerinfo
- name: PeerMetadata
  property_count: 1
  slug: qdrant-peermetadata
- name: PendingOptimization
  property_count: 2
  slug: qdrant-pendingoptimization
- name: PointGroup
  property_count: 3
  slug: qdrant-pointgroup
- name: PointIdsList
  property_count: 2
  slug: qdrant-pointidslist
- name: PointInsertOperations
  property_count: 0
  slug: qdrant-pointinsertoperations
- name: PointRequest
  property_count: 4
  slug: qdrant-pointrequest
- name: PointsBatch
  property_count: 4
  slug: qdrant-pointsbatch
- name: PointsList
  property_count: 4
  slug: qdrant-pointslist
- name: PointsSelector
  property_count: 0
  slug: qdrant-pointsselector
- name: PointStruct
  property_count: 3
  slug: qdrant-pointstruct
- name: PointVectors
  property_count: 2
  slug: qdrant-pointvectors
- name: PowExpression
  property_count: 1
  slug: qdrant-powexpression
- name: PowParams
  property_count: 2
  slug: qdrant-powparams
- name: Prefetch
  property_count: 8
  slug: qdrant-prefetch
- name: ProductQuantization
  property_count: 1
  slug: qdrant-productquantization
- name: ProductQuantizationConfig
  property_count: 2
  slug: qdrant-productquantizationconfig
- name: ProgressTree
  property_count: 7
  slug: qdrant-progresstree
- name: QuantizationConfig
  property_count: 0
  slug: qdrant-quantizationconfig
- name: QuantizationConfigDiff
  property_count: 0
  slug: qdrant-quantizationconfigdiff
- name: QuantizationSearchParams
  property_count: 3
  slug: qdrant-quantizationsearchparams
- name: Query
  property_count: 0
  slug: qdrant-query
- name: QueryGroupsRequest
  property_count: 14
  slug: qdrant-querygroupsrequest
- name: QueryInterface
  property_count: 0
  slug: qdrant-queryinterface
- name: QueryRequest
  property_count: 12
  slug: qdrant-queryrequest
- name: QueryRequestBatch
  property_count: 1
  slug: qdrant-queryrequestbatch
- name: QueryResponse
  property_count: 1
  slug: qdrant-queryresponse
- name: RaftInfo
  property_count: 6
  slug: qdrant-raftinfo
- name: Range
  property_count: 4
  slug: qdrant-range
- name: RangeInterface
  property_count: 0
  slug: qdrant-rangeinterface
- name: ReadConsistency
  property_count: 0
  slug: qdrant-readconsistency
- name: ReadConsistencyType
  property_count: 0
  slug: qdrant-readconsistencytype
- name: RecommendExample
  property_count: 0
  slug: qdrant-recommendexample
- name: RecommendGroupsRequest
  property_count: 15
  slug: qdrant-recommendgroupsrequest
- name: RecommendInput
  property_count: 3
  slug: qdrant-recommendinput
- name: RecommendQuery
  property_count: 1
  slug: qdrant-recommendquery
- name: RecommendRequest
  property_count: 13
  slug: qdrant-recommendrequest
- name: RecommendRequestBatch
  property_count: 1
  slug: qdrant-recommendrequestbatch
- name: RecommendStrategy
  property_count: 0
  slug: qdrant-recommendstrategy
- name: Record
  property_count: 5
  slug: qdrant-record
- name: RelevanceFeedbackInput
  property_count: 3
  slug: qdrant-relevancefeedbackinput
- name: RelevanceFeedbackQuery
  property_count: 1
  slug: qdrant-relevancefeedbackquery
- name: RemoteShardInfo
  property_count: 4
  slug: qdrant-remoteshardinfo
- name: RemoteShardTelemetry
  property_count: 4
  slug: qdrant-remoteshardtelemetry
- name: RenameAlias
  property_count: 2
  slug: qdrant-renamealias
- name: RenameAliasOperation
  property_count: 1
  slug: qdrant-renamealiasoperation
- name: Replica
  property_count: 2
  slug: qdrant-replica
- name: ReplicaSetTelemetry
  property_count: 6
  slug: qdrant-replicasettelemetry
- name: ReplicaState
  property_count: 0
  slug: qdrant-replicastate
- name: ReplicatePoints
  property_count: 3
  slug: qdrant-replicatepoints
- name: ReplicatePointsOperation
  property_count: 1
  slug: qdrant-replicatepointsoperation
- name: ReplicateShard
  property_count: 4
  slug: qdrant-replicateshard
- name: ReplicateShardOperation
  property_count: 1
  slug: qdrant-replicateshardoperation
- name: RequestsTelemetry
  property_count: 2
  slug: qdrant-requeststelemetry
- name: ReshardingDirection
  property_count: 0
  slug: qdrant-reshardingdirection
- name: ReshardingInfo
  property_count: 4
  slug: qdrant-reshardinginfo
- name: RestartTransfer
  property_count: 4
  slug: qdrant-restarttransfer
- name: RestartTransferOperation
  property_count: 1
  slug: qdrant-restarttransferoperation
- name: Rrf
  property_count: 2
  slug: qdrant-rrf
- name: RrfQuery
  property_count: 1
  slug: qdrant-rrfquery
- name: RunningEnvironmentTelemetry
  property_count: 9
  slug: qdrant-runningenvironmenttelemetry
- name: Sample
  property_count: 0
  slug: qdrant-sample
- name: SampleQuery
  property_count: 1
  slug: qdrant-samplequery
- name: ScalarQuantization
  property_count: 1
  slug: qdrant-scalarquantization
- name: ScalarQuantizationConfig
  property_count: 3
  slug: qdrant-scalarquantizationconfig
- name: ScalarType
  property_count: 0
  slug: qdrant-scalartype
- name: ScoredPoint
  property_count: 7
  slug: qdrant-scoredpoint
- name: ScrollRequest
  property_count: 7
  slug: qdrant-scrollrequest
- name: ScrollResult
  property_count: 2
  slug: qdrant-scrollresult
- name: SearchGroupsRequest
  property_count: 11
  slug: qdrant-searchgroupsrequest
- name: SearchMatrixOffsetsResponse
  property_count: 4
  slug: qdrant-searchmatrixoffsetsresponse
- name: SearchMatrixPair
  property_count: 3
  slug: qdrant-searchmatrixpair
- name: SearchMatrixPairsResponse
  property_count: 1
  slug: qdrant-searchmatrixpairsresponse
- name: SearchMatrixRequest
  property_count: 5
  slug: qdrant-searchmatrixrequest
- name: SearchParams
  property_count: 5
  slug: qdrant-searchparams
- name: SearchRequest
  property_count: 9
  slug: qdrant-searchrequest
- name: SearchRequestBatch
  property_count: 1
  slug: qdrant-searchrequestbatch
- name: SegmentConfig
  property_count: 3
  slug: qdrant-segmentconfig
- name: SegmentInfo
  property_count: 16
  slug: qdrant-segmentinfo
- name: SegmentTelemetry
  property_count: 4
  slug: qdrant-segmenttelemetry
- name: SegmentType
  property_count: 0
  slug: qdrant-segmenttype
- name: SetPayload
  property_count: 5
  slug: qdrant-setpayload
- name: SetPayloadOperation
  property_count: 1
  slug: qdrant-setpayloadoperation
- name: ShardCleanStatusFailedTelemetry
  property_count: 1
  slug: qdrant-shardcleanstatusfailedtelemetry
- name: ShardCleanStatusProgressTelemetry
  property_count: 1
  slug: qdrant-shardcleanstatusprogresstelemetry
- name: ShardCleanStatusTelemetry
  property_count: 0
  slug: qdrant-shardcleanstatustelemetry
- name: ShardingMethod
  property_count: 0
  slug: qdrant-shardingmethod
- name: ShardKey
  property_count: 0
  slug: qdrant-shardkey
- name: ShardKeyDescription
  property_count: 1
  slug: qdrant-shardkeydescription
- name: ShardKeySelector
  property_count: 0
  slug: qdrant-shardkeyselector
- name: ShardKeysResponse
  property_count: 1
  slug: qdrant-shardkeysresponse
- name: ShardKeyWithFallback
  property_count: 2
  slug: qdrant-shardkeywithfallback
- name: ShardSnapshotLocation
  property_count: 0
  slug: qdrant-shardsnapshotlocation
- name: ShardSnapshotRecover
  property_count: 4
  slug: qdrant-shardsnapshotrecover
- name: ShardStatus
  property_count: 0
  slug: qdrant-shardstatus
- name: ShardTransferInfo
  property_count: 7
  slug: qdrant-shardtransferinfo
- name: ShardTransferMethod
  property_count: 0
  slug: qdrant-shardtransfermethod
- name: ShardUpdateQueueInfo
  property_count: 3
  slug: qdrant-shardupdatequeueinfo
- name: SnapshotDescription
  property_count: 4
  slug: qdrant-snapshotdescription
- name: SnapshotPriority
  property_count: 0
  slug: qdrant-snapshotpriority
- name: SnapshotRecover
  property_count: 4
  slug: qdrant-snapshotrecover
- name: Snowball
  property_count: 0
  slug: qdrant-snowball
- name: SnowballLanguage
  property_count: 0
  slug: qdrant-snowballlanguage
- name: SnowballParams
  property_count: 2
  slug: qdrant-snowballparams
- name: SparseIndexConfig
  property_count: 3
  slug: qdrant-sparseindexconfig
- name: SparseIndexParams
  property_count: 3
  slug: qdrant-sparseindexparams
- name: SparseIndexType
  property_count: 0
  slug: qdrant-sparseindextype
- name: SparseVector
  property_count: 2
  slug: qdrant-sparsevector
- name: SparseVectorDataConfig
  property_count: 3
  slug: qdrant-sparsevectordataconfig
- name: SparseVectorParams
  property_count: 2
  slug: qdrant-sparsevectorparams
- name: SparseVectorsConfig
  property_count: 0
  slug: qdrant-sparsevectorsconfig
- name: SparseVectorStorageType
  property_count: 0
  slug: qdrant-sparsevectorstoragetype
- name: SqrtExpression
  property_count: 1
  slug: qdrant-sqrtexpression
- name: StartFrom
  property_count: 0
  slug: qdrant-startfrom
- name: StartResharding
  property_count: 3
  slug: qdrant-startresharding
- name: StartReshardingOperation
  property_count: 1
  slug: qdrant-startreshardingoperation
- name: StateRole
  property_count: 0
  slug: qdrant-staterole
- name: StemmingAlgorithm
  property_count: 0
  slug: qdrant-stemmingalgorithm
- name: StopwordsInterface
  property_count: 0
  slug: qdrant-stopwordsinterface
- name: StopwordsSet
  property_count: 2
  slug: qdrant-stopwordsset
- name: StrictModeConfig
  property_count: 20
  slug: qdrant-strictmodeconfig
- name: StrictModeConfigOutput
  property_count: 20
  slug: qdrant-strictmodeconfigoutput
- name: StrictModeMultivector
  property_count: 1
  slug: qdrant-strictmodemultivector
- name: StrictModeMultivectorConfig
  property_count: 0
  slug: qdrant-strictmodemultivectorconfig
- name: StrictModeMultivectorConfigOutput
  property_count: 0
  slug: qdrant-strictmodemultivectorconfigoutput
- name: StrictModeMultivectorOutput
  property_count: 1
  slug: qdrant-strictmodemultivectoroutput
- name: StrictModeSparse
  property_count: 1
  slug: qdrant-strictmodesparse
- name: StrictModeSparseConfig
  property_count: 0
  slug: qdrant-strictmodesparseconfig
- name: StrictModeSparseConfigOutput
  property_count: 0
  slug: qdrant-strictmodesparseconfigoutput
- name: StrictModeSparseOutput
  property_count: 1
  slug: qdrant-strictmodesparseoutput
- name: SumExpression
  property_count: 1
  slug: qdrant-sumexpression
- name: TelemetryData
  property_count: 7
  slug: qdrant-telemetrydata
- name: TextIndexParams
  property_count: 11
  slug: qdrant-textindexparams
- name: TextIndexType
  property_count: 0
  slug: qdrant-textindextype
- name: TokenizerType
  property_count: 0
  slug: qdrant-tokenizertype
- name: TrackerStatus
  property_count: 0
  slug: qdrant-trackerstatus
- name: TrackerTelemetry
  property_count: 7
  slug: qdrant-trackertelemetry
- name: UpdateCollection
  property_count: 8
  slug: qdrant-updatecollection
- name: UpdateMode
  property_count: 0
  slug: qdrant-updatemode
- name: UpdateOperation
  property_count: 0
  slug: qdrant-updateoperation
- name: UpdateOperations
  property_count: 1
  slug: qdrant-updateoperations
- name: UpdateQueueInfo
  property_count: 2
  slug: qdrant-updatequeueinfo
- name: UpdateResult
  property_count: 2
  slug: qdrant-updateresult
- name: UpdateStatus
  property_count: 0
  slug: qdrant-updatestatus
- name: UpdateVectors
  property_count: 3
  slug: qdrant-updatevectors
- name: UpdateVectorsOperation
  property_count: 1
  slug: qdrant-updatevectorsoperation
- name: UpsertOperation
  property_count: 1
  slug: qdrant-upsertoperation
- name: Usage
  property_count: 2
  slug: qdrant-usage
- name: UsingVector
  property_count: 0
  slug: qdrant-usingvector
- name: UuidIndexParams
  property_count: 4
  slug: qdrant-uuidindexparams
- name: UuidIndexType
  property_count: 0
  slug: qdrant-uuidindextype
- name: ValuesCount
  property_count: 4
  slug: qdrant-valuescount
- name: ValueVariants
  property_count: 0
  slug: qdrant-valuevariants
- name: Vector
  property_count: 0
  slug: qdrant-vector
- name: VectorDataConfig
  property_count: 7
  slug: qdrant-vectordataconfig
- name: VectorDataInfo
  property_count: 3
  slug: qdrant-vectordatainfo
- name: VectorIndexSearchesTelemetry
  property_count: 10
  slug: qdrant-vectorindexsearchestelemetry
- name: VectorInput
  property_count: 0
  slug: qdrant-vectorinput
- name: VectorOutput
  property_count: 0
  slug: qdrant-vectoroutput
- name: VectorParams
  property_count: 7
  slug: qdrant-vectorparams
- name: VectorParamsDiff
  property_count: 3
  slug: qdrant-vectorparamsdiff
- name: VectorsConfig
  property_count: 0
  slug: qdrant-vectorsconfig
- name: VectorsConfigDiff
  property_count: 0
  slug: qdrant-vectorsconfigdiff
- name: VectorStorageDatatype
  property_count: 0
  slug: qdrant-vectorstoragedatatype
- name: VectorStorageType
  property_count: 0
  slug: qdrant-vectorstoragetype
- name: VectorStruct
  property_count: 0
  slug: qdrant-vectorstruct
- name: VectorStructOutput
  property_count: 0
  slug: qdrant-vectorstructoutput
- name: VersionInfo
  property_count: 3
  slug: qdrant-versioninfo
- name: WalConfig
  property_count: 3
  slug: qdrant-walconfig
- name: WalConfigDiff
  property_count: 3
  slug: qdrant-walconfigdiff
- name: WebApiTelemetry
  property_count: 2
  slug: qdrant-webapitelemetry
- name: WithLookup
  property_count: 3
  slug: qdrant-withlookup
- name: WithLookupInterface
  property_count: 0
  slug: qdrant-withlookupinterface
- name: WithPayloadInterface
  property_count: 0
  slug: qdrant-withpayloadinterface
- name: WithVector
  property_count: 0
  slug: qdrant-withvector
- name: WriteOrdering
  property_count: 0
  slug: qdrant-writeordering
json_structures:
- name: Qdrant Structure
  property_count: 0
  slug: qdrant-structure
layout: provider
modified: '2026-05-19'
name: Qdrant
nav: Providers
network: true
overview: 'Qdrant publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Aliases API, Beta API, Collections API, and 6 more. Tagged areas include AI, Artificial Intelligence, and Vector Databases.


  The Qdrant catalog on APIs.io includes 1 Spectral governance ruleset.


  Qdrant''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Qdrant Plans Pricing
  plan_count: 5
  slug: qdrant-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 4
  name: Qdrant Rate Limits
  slug: qdrant-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Qdrant API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: qdrant-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.9
  delta: -5.9
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 62.5
    developer_ergonomics: 35.7
    discoverability: 63.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/qdrant/refs/heads/main/screenshots/qdrant-2026-06-20T192338.png
security:
- kind: authentication
  name: Qdrant Authentication
  slug: qdrant-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Qdrant Domain Security
  slug: qdrant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qdrant
tags:
- AI
- Artificial Intelligence
- Vector Databases
website: https://qdrant.tech
---
