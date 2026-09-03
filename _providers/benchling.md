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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 234
  human_in_the_loop: 0
  name: Benchling Agentic Access
  operation_count: 402
  slug: benchling-agentic-access
  summary_line: 402 operations · 234 acting
api_count: 2
apis:
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: AA Sequences are the working units of cells that make everything run (they help make structures, catalyze reactions and allow for signaling - a kind of internal cell communication). On Benchling, thes
  name: Benchling AA Sequences API
  slug: benchling-aa-sequences-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Create and manage Benchling apps on your tenant
  name: Benchling Apps API
  slug: benchling-apps-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Results represent the output of assays that have been performed. You can customize the schemas of results to fit your needs. Results can link to runs, entities, and other types. To learn more about cr
  name: Benchling Assay Results API
  slug: benchling-assay-results-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Runs capture the details / parameters of a run that was performed. Results are usually nested under a run.
  name: Benchling Assay Runs API
  slug: benchling-assay-runs-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Export audit log data for Benchling objects.
  name: Benchling Audit API
  slug: benchling-audit-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Endpoints to help authenticate with the rest of the API resources.
  name: Benchling Authentication API
  slug: benchling-authentication-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Blobs are opaque files that can be linked to other items in Benchling, like assay runs or results. For example, you can upload a blob, then upload an assay result that links to that blob by ID. The bl
  name: Benchling Blobs API
  slug: benchling-blobs-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Boxes are a structured inventory type, consisting of a grid of positions that can each hold one container. Unlike locations, there are a maximum number of containers that a box can hold (one per posit
  name: Benchling Boxes API
  slug: benchling-boxes-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Benchling curates codon usage data for a variety of organisms to support operations such as Codon Optimization and Back Translation.
  name: Benchling Codon Usage Tables API
  slug: benchling-codon-usage-tables-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Connect endpoints support Benchling Connect actions, like instrument data conversion.
  name: Benchling Connect API
  slug: benchling-connect-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Containers are the backbone of sample management in Benchling. They represent physical containers, such as tubes or wells, that hold quantities of biological samples (represented by the entities insid
  name: Benchling Containers API
  slug: benchling-containers-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Benchling supports custom entities for biological entities that are neither DNA, RNA, nor AA sequences. Custom entities must have an entity schema set and can have both schema fields and custom fields
  name: Benchling Custom Entities API
  slug: benchling-custom-entities-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Benchling allows users to configure their own fully-custom string representation formats for import/export of nucleotide sequences (including chemical modifications).
  name: Benchling Custom Notations API
  slug: benchling-custom-notations-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Data frames in Benchling represent tabular data that is not schematized. They contain columns with defined types and rows of data. Data frames are primarily used within specific Benchling applications
  name: Benchling Data Frames API
  slug: benchling-data-frames-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Similar to Data frames, datasets in Benchling represent tabular data that is not schematized. Datasets are saved to folders within Benchling with additional metadata, making them accessible and search
  name: Benchling Datasets API
  slug: benchling-datasets-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A DNA alignment is a Benchling object representing an alignment of multiple DNA sequences. This endpoint is deprecated, please migrate to the existing [Nucleotide Alignments endpoints.](#/Nucleotide%2
  name: Benchling DNA Alignments API
  slug: benchling-dna-alignments-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: DNA Oligos are short linear DNA sequences that can be attached as primers to full DNA sequences. Just like other entities, they support schemas, tags, and aliases.
  name: Benchling DNA Oligos API
  slug: benchling-dna-oligos-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: DNA sequences are the bread and butter of the Benchling Molecular Biology suite. On Benchling, these are comprised of a string of nucleotides and collections of other attributes, such as annotations a
  name: Benchling DNA Sequences API
  slug: benchling-dna-sequences-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Dropdowns are registry-wide enums. Use dropdowns to standardize on spelling and naming conventions, especially for important metadata like resistance markers.
  name: Benchling Dropdowns API
  slug: benchling-dropdowns-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Entities include DNA and AA sequences, oligos, molecules, custom entities, and other biological objects in Benchling. Entities support schemas, tags, and aliases, and can be registered.
  name: Benchling Entities API
  slug: benchling-entities-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Entries are rich text documents that allow you to capture all of your experimental data in one place.
  name: Benchling Entries API
  slug: benchling-entries-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Restriction enzymes are curated by Benchling for operations such as Digests and Codon Optimization.
  name: Benchling Enzymes API
  slug: benchling-enzymes-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The Events system allows external services to subscribe to events that are triggered in Benchling (e.g. plasmid registration, request submission, etc).
  name: Benchling Events API
  slug: benchling-events-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Export a Notebook Entry or a Legacy Workflow Stage Entry.
  name: Benchling Exports API
  slug: benchling-exports-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Feature Libraries are collections of shared canonical patterns that can be used to generate annotations on matching regions of DNA Sequences or AA Sequences.
  name: Benchling Feature Libraries API
  slug: benchling-feature-libraries-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Files are Benchling objects that represent files and their metadata. Compared to Blobs, which are used by most Benchling products for attachments, Files are primarily used in the Analysis and Connect '
  name: Benchling Files API
  slug: benchling-files-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Folders are nested within projects to provide additional organization.
  name: Benchling Folders API
  slug: benchling-folders-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Instrument Queries are used to query the instrument service.
  name: Benchling Instrument Queries API
  slug: benchling-instrument-queries-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Manage inventory wide objects.
  name: Benchling Inventory API
  slug: benchling-inventory-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Lab Automation endpoints support integration with lab instruments, and liquid handlers to create samples or results, and capture transfers between containers at scale.
  name: Benchling Lab Automation API
  slug: benchling-lab-automation-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: List label templates.
  name: Benchling Label Templates API
  slug: benchling-label-templates-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Legacy Requests allow scientists and teams to collaborate around experimental assays and workflows.
  name: Benchling Legacy Requests API
  slug: benchling-legacy-requests-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Legacy Workflows allow orchestrating complex experiments.
  name: Benchling Legacy Workflows API
  slug: benchling-legacy-workflows-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Please use endpoints for Legacy Workflows. These deprecated endpoints will be removed once users are migrated onto Legacy Workflows endpoints.
  name: Benchling Legacy Workflows (deprecated) API
  slug: benchling-legacy-workflows-deprecated-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Manage locations objects. Like all inventory, every Location has a barcode that is unique across the registry.
  name: Benchling Locations API
  slug: benchling-locations-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Mixtures are solutions comprised of multiple ingredients where the exact quantities of each ingredient are important to track. Each ingredient is uniquely identified by its component entity.
  name: Benchling Mixtures API
  slug: benchling-mixtures-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Molecules are groups of atoms held together by bonds, representing entities smaller than DNA Sequences and AA Sequences. Just like other entities, they support schemas, tags, and aliases.
  name: Benchling Molecules API
  slug: benchling-molecules-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Monomers are chemical building blocks with specified structures used to compose modified nucleotides. Note that monomer write endpoints require tenant admin permissions.
  name: Benchling Monomers API
  slug: benchling-monomers-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Nucleotide Alignment is a Benchling object representing an alignment of multiple DNA and/or RNA sequences.
  name: Benchling Nucleotide Alignments API
  slug: benchling-nucleotide-alignments-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Oligos are short linear DNA sequences that can be attached as primers to full DNA sequences. Just like other entities, they support schemas, tags, and aliases. Please migrate to the corresponding DNA '
  name: Benchling Oligos API
  slug: benchling-oligos-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: View organization objects.
  name: Benchling Organizations API
  slug: benchling-organizations-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Plates are a structured inventory type, grids of wells that each function like containers. Plates come in two types: a traditional "fixed" type, where the wells cannot move, and a "matrix" type. A mat'
  name: Benchling Plates API
  slug: benchling-plates-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: List printers.
  name: Benchling Printers API
  slug: benchling-printers-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Manage project objects.
  name: Benchling Projects API
  slug: benchling-projects-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Manage registry objects. See our documentation on [how to register entities](https://docs.benchling.com/docs/registering-entities).
  name: Benchling Registry API
  slug: benchling-registry-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: RNA Oligos are short linear RNA sequences that can be attached as primers to full DNA sequences. Just like other entities, they support schemas, tags, and aliases.
  name: Benchling RNA Oligos API
  slug: benchling-rna-oligos-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Chains of linear, single stranded RNA that support most capabilities and attributes of DNA Sequences.
  name: Benchling RNA Sequences API
  slug: benchling-rna-sequences-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Schemas represent custom configuration of objects in Benchling. See this [guide in our documentation](https://docs.benchling.com/docs/schemas) on how Schemas impact our developers
  name: Benchling Schemas API
  slug: benchling-schemas-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Endpoints that perform expensive computations launch long-running tasks. These endpoints return the task ID (a UUID) in the response body. After launching a task, periodically invoke the [Get a task](
  name: Benchling Tasks API
  slug: benchling-tasks-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: View team objects.
  name: Benchling Teams API
  slug: benchling-teams-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Manage user objects.
  name: Benchling Users API
  slug: benchling-users-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Manage warehouse credentials.
  name: Benchling Warehouse API
  slug: benchling-warehouse-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Workflow flowchart config versions are versioned graphs of flowchart configurations.
  name: Benchling Workflow Flowchart Config Versions API
  slug: benchling-workflow-flowchart-config-versions-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Workflow flowcharts represent the nodes and edges that a flowchart is comprised of.
  name: Benchling Workflow Flowcharts API
  slug: benchling-workflow-flowcharts-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Workflow outputs are outputs of a workflow task
  name: Benchling Workflow Outputs API
  slug: benchling-workflow-outputs-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Workflow task groups are groups of workflow tasks of the same schema
  name: Benchling Workflow Task Groups API
  slug: benchling-workflow-task-groups-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Workflow tasks encapsulate a single unit of work
  name: Benchling Workflow Tasks API
  slug: benchling-workflow-tasks-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents an amino acid sequence in Benchling's molecular biology platform. An AaSequence stores the one-letter amino acid code string along with annotations marking functional regions, domains, or o
  name: Benchling Aa Sequence API
  slug: benchling-aasequence-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for AA sequences.
  name: Benchling Aa Sequence Schema API
  slug: benchling-aasequenceschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The Agent API from Benchling — 1 operation(s) for agent.
  name: Benchling Agent API
  slug: benchling-agent-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Operations for Analysis
  name: Benchling Analysis API
  slug: benchling-analysis-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A reusable pipeline configuration that can be instantiated to create new Analysis objects. AnalysisTemplates define a complete data processing workflow with PipelineSteps (see `steps`) that can be par
  name: Benchling Analysis Template API
  slug: benchling-analysistemplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines a data frame placeholder within an AnalysisTemplate that users must provide when applying the template. Each variable specifies which PipelineStep input (replaceStep, replaceStepData, replaceS
  name: Benchling Analysis Template Data Frame Variable API
  slug: benchling-analysistemplatedataframevariable-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines a configuration parameter within an AnalysisTemplate that users can customize when applying the template. Unlike AnalysisTemplateDataFrameVariable which handles data frame inputs, this type re
  name: Benchling Analysis Template Variable API
  slug: benchling-analysistemplatevariable-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a Benchling App canvas, an embedded UI surface that apps use to render custom interactive content within notebook entries, entry templates, assay runs, or app homepages. Each canvas belongs
  name: Benchling App Canvas API
  slug: benchling-appcanvas-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Represents a configured value for a Benchling App on a specific tenant. Each config value has a path identifying its location in the configuration hierarchy and valueData containing the actual value. '
  name: Benchling App Config Value API
  slug: benchling-appconfigvalue-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents an installed Benchling App on a tenant, created from an `AppDefinitionVersion`. App installations store tenant-specific configuration values and feature bindings. As a Principal, app instal
  name: Benchling App Installation API
  slug: benchling-appinstallation-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a running or completed session for a Benchling App. App sessions track long-running app operations, providing status updates and user-facing messages. Each session belongs to a single app i
  name: Benchling App Session API
  slug: benchling-appsession-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a molecular cloning assembly that combines multiple DNA fragments into complete constructs. Assemblies model the process of joining fragment sequences (such as genes, promoters, and termina
  name: Benchling Assembly API
  slug: benchling-assembly-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a single entry in an object's audit log. Each entry captures what changed, who made the change, and contextual information about the affected object hierarchy.
  name: Benchling Audit Log API
  slug: benchling-auditlog-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Box is a grid-based storage container in Benchling's inventory system, designed to hold multiple sample containers (tubes, vials, etc.) in an organized layout. Boxes have a defined capacity based on
  name: Benchling Box API
  slug: benchling-box-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure and constraints for a category of Boxes in Benchling's inventory system. A BoxSchema specifies the grid dimensions (height and width) determining how many container positions the
  name: Benchling Box Schema API
  slug: benchling-boxschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The BulkExport API from Benchling — 1 operation(s) for bulkexport.
  name: Benchling Bulk Export API
  slug: benchling-bulkexport-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Chart is a data visualization within Benchling. Charts can be created directly (for example, via APIs or the UI) or generated from other workflows. Charts store their configuration in a library-spec
  name: Benchling Chart API
  slug: benchling-chart-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Collaboration indicates that a Principal or Group is granted a Policy on a Resource. Some Collaborations represent Ownership, while others indicate that a Resource was shared with the Principal or G
  name: Benchling Collaboration API
  slug: benchling-collaboration-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Records a configuration import operation from one Benchling tenant to another. Each entry captures the source tenant, target organization, who performed the import, and an optional changelog URL docum
  name: Benchling Config Import History Entry API
  slug: benchling-configimporthistoryentry-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'A Container is a physical vessel (such as a tube, vial, or cryotube) that holds biological or chemical samples in Benchling''s inventory system. Containers track their contents (see ContainerContent), '
  name: Benchling Container API
  slug: benchling-container-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Defines the structure and metadata for a category of Containers in Benchling''s inventory system. A `ContainerSchema` specifies the container type (e.g., "1.5mL Microcentrifuge Tube", "2mL Cryovial"), '
  name: Benchling Container Schema API
  slug: benchling-containerschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A flexible, user-defined entity type in Benchling's Registry. Unlike specialized entity types such as DnaSequence or Molecule, CustomEntities allow organizations to model any kind of scientific or bus
  name: Benchling Custom Entity API
  slug: benchling-customentity-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Operations for CustomEntitySchema
  name: Benchling Custom Entity Schema API
  slug: benchling-customentityschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: '`DataFrame` stores non-schematized tabular data, with Benchling-aware column types (see `DataFrameColumn`). Data frames are not searchable and lack their own permissions; rather, they are child object'
  name: Benchling Data Frame API
  slug: benchling-dataframe-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: '`Dataset` stores non-schematized tabular data, with Benchling-aware column types. Datasets are first-class, searchable, archivable folder items. A Dataset''s actual data is stored in a `DataFrame`.'
  name: Benchling Dataset API
  slug: benchling-dataset-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a short single-stranded DNA oligonucleotide in Benchling's molecular biology platform. DNA oligos are typically synthetic sequences used as primers for PCR, probes for hybridization assays,
  name: Benchling Dna Oligo API
  slug: benchling-dnaoligo-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for DNA oligos.
  name: Benchling Dna Oligo Schema API
  slug: benchling-dnaoligoschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a DNA sequence in Benchling's molecular biology platform. A `DnaSequence` stores the nucleotide bases of the forward strand along with rich annotations for biological features such as genes
  name: Benchling Dna Sequence API
  slug: benchling-dnasequence-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for DNA sequences.
  name: Benchling Dna Sequence Schema API
  slug: benchling-dnasequenceschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The DocumentExport API from Benchling — 3 operation(s) for documentexport.
  name: Benchling Document Export API
  slug: benchling-documentexport-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents an ordered piece of content within an entry, template, subtemplate, or document. Each document part wraps one content block and records its container, version, and audit metadata.
  name: Benchling Document Part API
  slug: benchling-documentpart-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A configurable list of predefined values used for standardizing data entry in schema fields. Dropdowns provide controlled vocabulary choices that ensure consistency when users fill out entity and obje
  name: Benchling Dropdown API
  slug: benchling-dropdown-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A schema field definition that links to a dropdown for value selection. The `linkDefinition` field references the `Dropdown` configuration that defines the available options. When `isMulti` is true, u
  name: Benchling Dropdown Link Field Definition API
  slug: benchling-dropdownlinkfielddefinition-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'An individual selectable value within a Dropdown. Each DropdownOption represents one valid choice that users can select when populating a schema field configured with the parent Dropdown. Options can '
  name: Benchling Dropdown Option API
  slug: benchling-dropdownoption-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure and behavior for a category of registered entities in Benchling. EntitySchemas specify the field definitions (see `fieldDefinitions` and `SchemaFieldDefinition`) that determine w
  name: Benchling Entity Schema API
  slug: benchling-entityschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'An Entry is the core document type in Benchling''s Electronic Lab Notebook (ELN), used by scientists to record experimental work and observations. Entries are organized into sections (days) containing '
  name: Benchling Entry API
  slug: benchling-entry-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines a schema that can be applied to Entries to add structured metadata through custom fields. Entry schemas allow organizations to standardize the information captured in notebook entries by defin
  name: Benchling Entry Schema API
  slug: benchling-entryschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A reusable content block that can be inserted into `DocumentLike` objects. Subtemplates contain pre-defined note content (text, tables, etc.) that scientists commonly need to repeat across multiple en
  name: Benchling Entry Subtemplate API
  slug: benchling-entrysubtemplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A template used to create new `DocumentLike` objects with pre-populated content and structure. `EntryTemplate`s contain boilerplate text, tables, placeholders, and other note content that provides a c
  name: Benchling Entry Template API
  slug: benchling-entrytemplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a restriction enzyme from Benchling's global catalog of commercially available enzymes. Restriction enzymes (also known as restriction endonucleases) are molecular scissors that recognize s
  name: Benchling Enzyme API
  slug: benchling-enzyme-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a user-curated collection of restriction enzymes for molecular cloning workflows. EnzymeLists allow users and organizations to organize commonly used enzymes into named groups for easy acce
  name: Benchling Enzyme List API
  slug: benchling-enzymelist-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for Equipments.
  name: Benchling Equipment Schema API
  slug: benchling-equipmentschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Configures delivery of Benchling events to external systems via AWS EventBridge. Event subscriptions enable real-time integration by streaming events (such as entity creation, updates, or workflow sta
  name: Benchling Event Subscription API
  slug: benchling-eventsubscription-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a reusable collection of biological features for auto-annotating nucleotide and AA sequences. FeatureLibraries enable users to define common sequence motifs (such as genes, promoters, termi
  name: Benchling Feature Library API
  slug: benchling-featurelibrary-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a single feature definition within a FeatureLibrary used for auto-annotation. Each item defines a searchable pattern (nucleotide or amino acid sequence), a feature type classification (such
  name: Benchling Feature Library Item API
  slug: benchling-featurelibraryitem-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A tenant-defined schema interface (also known as a "Fieldset") that groups related fields to be shared across multiple schemas. Fieldsets are created and managed by tenant administrators and belong to
  name: Benchling Fieldset API
  slug: benchling-fieldset-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A File represents an uploaded document or data file that is surfaced in Benchling's Data Catalog for discovery and organization. Files are primarily created through Benchling Connect (for external fil
  name: Benchling File API
  slug: benchling-file-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A hierarchical container for organizing entities, notebook entries, and other items within a Project. Folders support nested structures through parent-child relationships (see `parent`), enabling user
  name: Benchling Folder API
  slug: benchling-folder-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A database of reference sequences used to characterize protein sequences via alignment.
  name: Benchling Germline API
  slug: benchling-germline-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Indicates that a Principal is a member of Group. Role indicates that the Principal is a member of a subgroup, such as Admins of the Group. Teams are the canonical example of a Group.
  name: Benchling Group Membership API
  slug: benchling-groupmembership-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A `LabelTemplate` defines the format for printing physical labels for inventory items, such as containers, plates, and boxes. Each template contains a template string, `zplTemplate`, that is populated
  name: Benchling Label Template API
  slug: benchling-labeltemplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a legacy (pre-App Store) Benchling App installation on a tenant. Legacy apps are configured directly with webhook URLs and configuration specs rather than through app definition versions. T
  name: Benchling Legacy App Installation API
  slug: benchling-legacyappinstallation-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A reusable parameter definition stored in the Parameter Library. LibraryParameterDefinitions allow organizations to standardize parameters used across multiple procedures by defining a name, descripti
  name: Benchling Library Parameter Definition API
  slug: benchling-libraryparameterdefinition-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The limits API from Benchling — 1 operation(s) for limits.
  name: Benchling Limits API
  slug: benchling-limits-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Location represents a physical storage area in Benchling's inventory system, such as a freezer, refrigerator, shelf, room, or building. Locations form a hierarchy where each location can contain chi
  name: Benchling Location API
  slug: benchling-location-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure and metadata for a category of Locations in Benchling's inventory system. A LocationSchema specifies schema field definitions for capturing location-specific data (e.g., temperat
  name: Benchling Location Schema API
  slug: benchling-locationschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A MatrixPlate is a rack-style storage plate where Containers (tubes, vials) can be inserted into and removed from grid positions. Unlike FixedPlate or WellPlate where wells are permanently attached, M
  name: Benchling Matrix Plate API
  slug: benchling-matrixplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Defines the structure and constraints for a category of MatrixPlates in Benchling''s inventory system. A MatrixPlateSchema specifies the grid dimensions (height and width), an optional ContainerSchema '
  name: Benchling Matrix Plate Schema API
  slug: benchling-matrixplateschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Mixture is a formulation entity in Benchling that represents a combination of ingredients with specified amounts. Mixtures are commonly used for buffers, media, reagent preparations, and other multi
  name: Benchling Mixture API
  slug: benchling-mixture-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for Mixtures.
  name: Benchling Mixture Schema API
  slug: benchling-mixtureschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Molecule represents a small molecule chemical compound in Benchling that is imported either as a MolFile or using SMILES (Simplified Molecular Input Line Entry System) notation. Molecules are regist
  name: Benchling Molecule API
  slug: benchling-molecule-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for Molecule schemas.
  name: Benchling Molecule Schema API
  slug: benchling-moleculeschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a multiple sequence alignment of nucleotide sequences (DNA or RNA). Nucleotide alignments are used to compare sequence reads against a reference template for verification (see AlignmentType
  name: Benchling Nucleotide Alignment API
  slug: benchling-nucleotidealignment-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A building block component of modified oligonucleotides, representing a sugar, phosphate, or base subunit. Monomers are the chemical units that assemble to form nucleotides in therapeutic oligonucleot
  name: Benchling Nucleotide Monomer API
  slug: benchling-nucleotidemonomer-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'An oligo conjugate is a therapeutic modality consisting of a single-stranded oligonucleotide backbone with one or more attached conjugate molecules. Common examples include antisense oligonucleotides '
  name: Benchling Oligo Conjugate API
  slug: benchling-oligoconjugate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for Oligo Conjugates.
  name: Benchling Oligo Conjugate Schema API
  slug: benchling-oligoconjugateschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: An oligo duplex is a therapeutic modality consisting of two complementary oligonucleotide strands (forward and reverse) with optional conjugate molecules attached to either strand. The classic example
  name: Benchling Oligo Duplex API
  slug: benchling-oligoduplex-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for Oligo Duplexes.
  name: Benchling Oligo Duplex Schema API
  slug: benchling-oligoduplexschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Represents a group of users within Benchling, typically corresponding to a company, department, or research group. Organizations provide a many-to-many relationship between users—each user can belong '
  name: Benchling Organization API
  slug: benchling-organization-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a single operation node within a Pipeline's directed acyclic graph (DAG). Each step performs a specific transformation determined by its stepType (see `PipelineStepType`), with configuratio
  name: Benchling Pipeline Step API
  slug: benchling-pipelinestep-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents actual data attached to an input or output slot of a PipelineStep during execution. Each PipelineStepData corresponds to a defined data shape (input or output) on the step's configuration a
  name: Benchling Pipeline Step Data API
  slug: benchling-pipelinestepdata-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Plate is a legacy unified type representing both well plates and tube racks in Benchling's inventory system. The type field (see PlateType) indicates whether this is a FIXED_PLATE (wells permanently
  name: Benchling Plate API
  slug: benchling-plate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A named plate design template backed by a scratch plate that lives in a template collection. Plate design templates allow scratch plates to be organized and reused as templates.
  name: Benchling Plate Design Template API
  slug: benchling-platedesigntemplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure and constraints for a category of Plates in Benchling's inventory system. A PlateSchema specifies the grid dimensions (height and width), the plate type (see PlateType), and opti
  name: Benchling Plate Schema API
  slug: benchling-plateschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines a named set of permissions that can be assigned to users or groups through collaborations. Policies contain PolicyStatements that specify allowed actions on different item types. When a user i
  name: Benchling Policy API
  slug: benchling-policy-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents an execution of a Model Hub model against multiple data inputs (resulting in multiple Predictions). A PredictionBatch tracks the input configuration, execution status, and results. Each bat
  name: Benchling Prediction Batch API
  slug: benchling-predictionbatch-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a single prediction within a PredictionBatch. Each PredictionJob captures the input configuration for one prediction and its association with input components (e.g., AA sequences, molecules
  name: Benchling Prediction Job API
  slug: benchling-predictionjob-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Printer represents a network-connected label printer configured in Benchling for printing barcode labels on inventory items. Printers are associated with a Registry and work with LabelTemplates to g
  name: Benchling Printer API
  slug: benchling-printer-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A reusable template that defines a structured experimental workflow. Procedures specify a sequence of method steps (see `ProcedureMethodDefinitionVersion`) connected in a flowchart (see `workflowFlowc
  name: Benchling Procedure API
  slug: benchling-procedure-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Contains the flowchart configuration for a Procedure or TemplateCollection. A ProcedureFlowchart acts as a container for flowchart versions (see `ProcedureFlowchartVersion`), tracking both the latest '
  name: Benchling Procedure Flowchart API
  slug: benchling-procedureflowchart-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a snapshot of a procedure's flowchart configuration at a specific point in time. The flowchart defines the structure of a procedure as a directed graph, where nodes represent method steps (
  name: Benchling Procedure Flowchart Config Version Proxy API
  slug: benchling-procedureflowchartconfigversionproxy-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: An immutable snapshot of a procedure's flowchart structure at a specific point in time. Each version contains the complete graph of method steps (see `nodes` and `ProcedureMethodDefinitionVersion`) an
  name: Benchling Procedure Flowchart Version API
  slug: benchling-procedureflowchartversion-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'A versioned method within a procedure flowchart. Methods are the building blocks of procedures, representing discrete experimental operations that scientists perform. Each method contains step groups '
  name: Benchling Procedure Method Definition Version API
  slug: benchling-proceduremethoddefinitionversion-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: An instance of a method being executed within a procedure run. When a scientist runs a procedure, each method in the flowchart becomes a ProcedureMethodExecutionInstance that tracks the actual executi
  name: Benchling Procedure Method Execution Instance API
  slug: benchling-proceduremethodexecutioninstance-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Links two method execution instances across procedure runs to represent an intended connection within a study. This allows scientists to coordinate their analyses across runs, even when the flowchart '
  name: Benchling Procedure Method Execution Instance Association API
  slug: benchling-proceduremethodexecutioninstanceassociation-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a parameter entity within a procedure template. Parameters define the data, materials, or equipment that scientists interact with during procedure execution. The `parameterType` field class
  name: Benchling Procedure Parameter API
  slug: benchling-procedureparameter-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Records a scientist''s confirmation of a parameter value during procedure execution. When running a procedure, scientists confirm that inputs (such as materials, equipment, or data) match expectations '
  name: Benchling Procedure Parameter Confirmation Value API
  slug: benchling-procedureparameterconfirmationvalue-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Records the actual measured or observed value for a parameter during procedure execution. Scientists enter measured values after performing an experimental step—for example, recording a temperature re
  name: Benchling Procedure Parameter Measured Value API
  slug: benchling-procedureparametermeasuredvalue-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Stores the expected or planned value for a parameter, set during procedure setup or run planning. Used to specify anticipated inputs before execution begins—for example, the target concentration for a
  name: Benchling Procedure Parameter Planned Value API
  slug: benchling-procedureparameterplannedvalue-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A versioned definition of a procedure parameter. Each version specifies the parameter's name, description, data type configuration (`dataType`), and how values are entered (`confirmationMethod`). Para
  name: Benchling Procedure Parameter Version API
  slug: benchling-procedureparameterversion-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: An active execution of a procedure template. Created when scientists start running an experiment based on a `Procedure`. Contains experimental conditions (`conditions` via `ProcedureRunCondition`) and
  name: Benchling Procedure Run API
  slug: benchling-procedurerun-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A ProcedureRunCondition represents a configuration of the methods of a Procedure that is being executed within a ProcedureRun. The values associated with the ProcedureRunCondition are not exposed on t
  name: Benchling Procedure Run Condition API
  slug: benchling-procedureruncondition-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A replicate of a `ProcedureRunCondition`, representing one execution of a condition's configuration. Scientists often run the same experimental condition multiple times to obtain statistically signifi
  name: Benchling Procedure Run Condition Replicate API
  slug: benchling-procedurerunconditionreplicate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A draft experiment plan that can be promoted to a `ProcedureRun` for execution. Scientists use run plans to configure experimental conditions, parameter values, and replicates before starting an actua
  name: Benchling Procedure Run Plan API
  slug: benchling-procedurerunplan-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A planned experimental condition within a `ProcedureRunPlan`, representing how a procedure's methods will be configured when the plan is promoted to an actual `ProcedureRun`. Each condition contains p
  name: Benchling Procedure Run Plan Condition API
  slug: benchling-procedurerunplancondition-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A versioned definition of a procedure step within a procedure flowchart. Steps represent documentation or instructions that guide scientists through a procedure but do not collect data—they differ fro
  name: Benchling Procedure Step Definition Version API
  slug: benchling-procedurestepdefinitionversion-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: An execution instance of a procedure step within a `ProcedureMethodExecutionInstance`. Created when a procedure run is started, representing a step where scientists can document their work. The `docum
  name: Benchling Procedure Step Execution Instance API
  slug: benchling-procedurestepexecutioninstance-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A top-level organizational container in Benchling that groups related work and controls access permissions. Projects contain Folders (see `Folder`) which in turn hold entities, notebook entries, and o
  name: Benchling Project API
  slug: benchling-project-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Protein is a complex biomolecule entity in Benchling representing immunoglobulins or related therapeutic proteins like T-cell receptors. Proteins are defined by an `ProteinFormat` that specifies the
  name: Benchling Protein API
  slug: benchling-protein-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A ProteinFormat defines the structural template for a class of proteins, specifying the arrangement of chains and domains. Formats can be built-in (e.g., IgG1, Fab, scFv) or custom-defined by users.
  name: Benchling Protein Format API
  slug: benchling-proteinformat-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for Proteins.
  name: Benchling Protein Schema API
  slug: benchling-proteinschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A historical snapshot of an `Protein` at a specific point in time, preserving the complete structural state including domains, chains, and HELM notation. Protein versions form a lineage that tracks ch
  name: Benchling Protein Version API
  slug: benchling-proteinversion-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Chemical Reaction is a process where molecules are transformed into new molecules.
  name: Benchling Reaction API
  slug: benchling-reaction-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A reusable template that defines the structure and configuration for requests in Benchling. Also known as a "Request Template" in the UI. Each RequestV2Definition specifies a `templateDocument` that s
  name: Benchling Request V2 Definition API
  slug: benchling-requestv2definition-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A workflow request submitted from a `RequestV2Definition` (known as "Request Template" in the UI). When a request is submitted (status transitions to SENT), a `WorkflowTaskGroup` is automatically crea
  name: Benchling Request V2 Submission API
  slug: benchling-requestv2submission-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Result represents a single row of experimental measurement data in Benchling's lab automation system. Results conform to a ResultSchema that defines their field structure, enabling standardized capt
  name: Benchling Result API
  slug: benchling-result-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure and metadata fields for a category of assay Results in Benchling's lab automation system. A ResultSchema specifies the field definitions that capture measurement data, calculated
  name: Benchling Result Schema API
  slug: benchling-resultschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents an active or completed review of a reviewable item such as an Entry or StageEntry. A Review tracks the overall status, the assigned reviewers (see `Reviewer`), and links back to the reviewa
  name: Benchling Review API
  slug: benchling-review-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a single action taken within a review. ReviewChanges form an ordered history of all changes made to a review, including status transitions, reviewer assignments, and comments. Each ReviewCh
  name: Benchling Review Change API
  slug: benchling-reviewchange-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines a review process configuration that specifies how entries and other reviewable items should be reviewed. A ReviewProcess belongs to an Organization and can be associated with one or more Proje
  name: Benchling Review Process API
  slug: benchling-reviewprocess-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A single stage within a ReviewProcess that defines a required step in the review workflow. Each stage specifies what action reviewers must take (see `ReviewProcessActionType`), who is eligible to be a
  name: Benchling Review Process Stage API
  slug: benchling-reviewprocessstage-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a short single-stranded RNA oligonucleotide in Benchling's molecular biology platform. RNA oligos are synthetic sequences used in applications such as RNA interference (siRNA, shRNA), antis
  name: Benchling Rna Oligo API
  slug: benchling-rnaoligo-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for RNA oligos.
  name: Benchling Rna Oligo Schema API
  slug: benchling-rnaoligoschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents an RNA sequence in Benchling's molecular biology platform. An RnaSequence stores the nucleotide bases (using A, C, G, U) along with annotations marking functional regions, translation annot
  name: Benchling Rna Sequence API
  slug: benchling-rnasequence-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure, field definitions, and configuration options for RNA sequences
  name: Benchling Rna Sequence Schema API
  slug: benchling-rnasequenceschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Run represents an execution instance of a lab automation workflow in Benchling, capturing the inputs, outputs, and metadata for a single assay or instrument operation. Runs conform to a RunSchema th
  name: Benchling Run API
  slug: benchling-run-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure and automation configuration for a category of Runs in Benchling's lab automation system. A RunSchema specifies field definitions for run metadata, input generator configurations
  name: Benchling Run Schema API
  slug: benchling-runschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A ScratchFile represents raw file content used as intermediate input or output of pipeline steps (see PipelineStepData). Unlike File, ScratchFiles are not surfaced in the Data Catalog because they typ
  name: Benchling Scratch File API
  slug: benchling-scratchfile-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'A plate design or record used for designing, tracking, and analyzing experimental plates outside of the inventory. Scratch plates are the working surface for plate-based workflows: you build up a plat'
  name: Benchling Scratch Plate API
  slug: benchling-scratchplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The Search API from Benchling — 1 operation(s) for search.
  name: Benchling Search API
  slug: benchling-search-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a non-human identity used for system integrations and automated processes within Benchling. Service principals act as the identity for service accounts that perform actions via APIs or back
  name: Benchling Service Principal API
  slug: benchling-serviceprincipal-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A SqlDashboard is a configurable analytics page that displays one or more SQL-driven visualizations within Benchling Insights. Dashboards belong to a Project and contain ordered blocks (see SqlDashboa
  name: Benchling Sql Dashboard API
  slug: benchling-sqldashboard-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Represents a single query and visualization pane within a SqlDashboard. Each block contains a SQL query (sqlQuery) that runs against the Benchling data warehouse, along with a BlockVisualization that '
  name: Benchling Sql Dashboard Block API
  slug: benchling-sqldashboardblock-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A StageEntry is an Entry that is associated with a specific stage in a legacy Workflow. Unlike regular Entries which exist independently in folders, StageEntries are created as part of workflow execut
  name: Benchling Stage Entry API
  slug: benchling-stageentry-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A structured unit used to plan and organize research in Benchling. Each study progresses through phases (see `StudyPhase`) sequentially from design to execution to completion. The current phase determ
  name: Benchling Study API
  slug: benchling-study-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents the link between a Study and a Studyable item (such as entities or molecules). Each association is identified by id and links a specific `study` to a specific `item`, and records when the l
  name: Benchling Study Item Association API
  slug: benchling-studyitemassociation-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A configuration template that defines the structure and behavior of Studies within an organization. Each `StudySchema` specifies the `studyType`, which determines available features and workflow capab
  name: Benchling Study Schema API
  slug: benchling-studyschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a subgroup of users within an `Organization`, enabling finer-grained user management and data sharing. Teams belong to exactly one organization, and users may only join a team if they are a
  name: Benchling Team API
  slug: benchling-team-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A container that organizes related templates, subtemplates, and other template-like items. Template Collections provide a way to group and manage reusable content that teams use to create standardized
  name: Benchling Template Collection API
  slug: benchling-templatecollection-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Test Definition is a configuration object that specifies a type of test or assay that can be ordered against samples. Each Test Definition is associated with a `ResultSchema` that defines the struct
  name: Benchling Test Definition API
  slug: benchling-testdefinition-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A Test Order represents an individual request to perform a specific test on a sample. Each Test Order references a `TestDefinition` that specifies what type of test to perform, and a `sample` (Entity)
  name: Benchling Test Order API
  slug: benchling-testorder-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'A Unit is a specific measure of a physical quantity within Benchling''s tenant-specific unit dictionary, used to capture and convert scientific measurements across the platform. Each Unit belongs to a '
  name: Benchling Unit API
  slug: benchling-unit-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A UnitType is a dimensional category that groups inter-convertible `Unit` objects within Benchling's tenant-specific unit dictionary. Examples include Volume, Mass, Time, Molar Concentration, and cust
  name: Benchling Unit Type API
  slug: benchling-unittype-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a human user in Benchling who can log in, perform actions, and own data. Users belong to one or more Organizations and may be members of Teams within those organizations. As an Owner, users
  name: Benchling User API
  slug: benchling-user-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: 'Represents credentials for connecting to Benchling''s data warehouse, enabling users to query data using SQL tools like database clients or BI platforms. This includes all warehouse login types: user-g'
  name: Benchling Warehouse Credential API
  slug: benchling-warehousecredential-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A custom SQL view created by users in Benchling's data warehouse, allowing them to define reusable queries that can be accessed like tables. Views appear in a dedicated schema and can be queried via I
  name: Benchling Warehouse Custom View API
  slug: benchling-warehousecustomview-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A WellPlate is a multi-well plate in Benchling's inventory system where wells are permanently fixed to the plate structure. This is the standard plate type for laboratory multi-well formats such as 96
  name: Benchling Well Plate API
  slug: benchling-wellplate-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a single well within a WellPlate, functioning as a fixed container at a specific grid position. Each WellPlatePosition has coordinates identifying its row and column, can hold sample conten
  name: Benchling Well Plate Position API
  slug: benchling-wellplateposition-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure and constraints for a category of WellPlates in Benchling's inventory system. A WellPlateSchema specifies the grid dimensions (height and width) determining how many wells the pl
  name: Benchling Well Plate Schema API
  slug: benchling-wellplateschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents the result or product of completing a `WorkflowTask`. Each output is associated with a single task. Outputs can contain schema-defined fields that capture structured data from task executio
  name: Benchling Workflow Output API
  slug: benchling-workflowoutput-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Defines the structure of `WorkflowOutput` instances produced by tasks of a given `WorkflowTaskSchema`. Each output schema specifies `fieldDefinitions` for the data to be captured, an optional `prefix`
  name: Benchling Workflow Output Schema API
  slug: benchling-workflowoutputschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Represents a unit of work within a `WorkflowTaskGroup`. Each task has a `status` that progresses through a configurable lifecycle (see `WorkflowTaskStatusLifecycle`), an optional `assignee` and `respo
  name: Benchling Workflow Task API
  slug: benchling-workflowtask-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A container that groups related `WorkflowTask` instances together, representing a cohesive unit of work. Task groups are created from a `WorkflowTaskSchema` (via `workflowTaskSchema`). They are stored
  name: Benchling Workflow Task Group API
  slug: benchling-workflowtaskgroup-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A configuration template that defines the structure and behavior of `WorkflowTask` instances. Each schema specifies an `executionType` (direct, entry, or flowchart) and custom `fieldDefinitions` for t
  name: Benchling Workflow Task Schema API
  slug: benchling-workflowtaskschema-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A typed collection of items used to group related objects for batch operations. Unlike folders, items can belong to multiple worklists simultaneously, making worklists useful as temporary holding grou
  name: Benchling Worklist API
  slug: benchling-worklist-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: A structured document container used to organize and execute procedural work within Benchling's notebook system. Worksheets contain ordered `WorksheetStepGroup`s, each holding `WorksheetStep`s that re
  name: Benchling Worksheet API
  slug: benchling-worksheet-api
artifact_total: 1142
asyncapis:
- description: ''
  name: Benchling Webhooks
  slug: benchling-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Benchling AA Sequences API
  slug: open-benchling-aa-sequences-api
- collection_type: open
  name: Benchling AA Sequences Apps API
  slug: open-benchling-apps-api
- collection_type: open
  name: Benchling AA Sequences Assay Results API
  slug: open-benchling-assay-results-api
- collection_type: open
  name: Benchling AA Sequences Assay Runs API
  slug: open-benchling-assay-runs-api
- collection_type: open
  name: Benchling AA Sequences Audit API
  slug: open-benchling-audit-api
- collection_type: open
  name: Benchling AA Sequences Authentication API
  slug: open-benchling-authentication-api
- collection_type: open
  name: Benchling AA Sequences Blobs API
  slug: open-benchling-blobs-api
- collection_type: open
  name: Benchling AA Sequences Boxes API
  slug: open-benchling-boxes-api
- collection_type: open
  name: Benchling AA Sequences Codon Usage Tables API
  slug: open-benchling-codon-usage-tables-api
- collection_type: open
  name: Benchling AA Sequences Connect API
  slug: open-benchling-connect-api
- collection_type: open
  name: Benchling AA Sequences Containers API
  slug: open-benchling-containers-api
- collection_type: open
  name: Benchling AA Sequences Custom Entities API
  slug: open-benchling-custom-entities-api
- collection_type: open
  name: Benchling AA Sequences Custom Notations API
  slug: open-benchling-custom-notations-api
- collection_type: open
  name: Benchling AA Sequences Data Frames API
  slug: open-benchling-data-frames-api
- collection_type: open
  name: Benchling AA Sequences Datasets API
  slug: open-benchling-datasets-api
- collection_type: open
  name: Benchling AA Sequences DNA Alignments API
  slug: open-benchling-dna-alignments-api
- collection_type: open
  name: Benchling AA Sequences DNA Oligos API
  slug: open-benchling-dna-oligos-api
- collection_type: open
  name: Benchling AA Sequences DNA Sequences API
  slug: open-benchling-dna-sequences-api
- collection_type: open
  name: Benchling AA Sequences Dropdowns API
  slug: open-benchling-dropdowns-api
- collection_type: open
  name: Benchling AA Sequences Entities API
  slug: open-benchling-entities-api
- collection_type: open
  name: Benchling AA Sequences Entries API
  slug: open-benchling-entries-api
- collection_type: open
  name: Benchling AA Sequences Enzymes API
  slug: open-benchling-enzymes-api
- collection_type: open
  name: Benchling AA Sequences Events API
  slug: open-benchling-events-api
- collection_type: open
  name: Benchling AA Sequences Exports API
  slug: open-benchling-exports-api
- collection_type: open
  name: Benchling AA Sequences Feature Libraries API
  slug: open-benchling-feature-libraries-api
- collection_type: open
  name: Benchling AA Sequences Files API
  slug: open-benchling-files-api
- collection_type: open
  name: Benchling AA Sequences Folders API
  slug: open-benchling-folders-api
- collection_type: open
  name: Benchling AA Sequences Instrument Queries API
  slug: open-benchling-instrument-queries-api
- collection_type: open
  name: Benchling AA Sequences Inventory API
  slug: open-benchling-inventory-api
- collection_type: open
  name: Benchling AA Sequences Lab Automation API
  slug: open-benchling-lab-automation-api
- collection_type: open
  name: Benchling AA Sequences Label Templates API
  slug: open-benchling-label-templates-api
- collection_type: open
  name: Benchling AA Sequences Legacy Requests API
  slug: open-benchling-legacy-requests-api
- collection_type: open
  name: Benchling AA Sequences Legacy Workflows API
  slug: open-benchling-legacy-workflows-api
- collection_type: open
  name: Benchling AA Sequences Legacy Workflows (deprecated) API
  slug: open-benchling-legacy-workflows-deprecated-api
- collection_type: open
  name: Benchling AA Sequences Locations API
  slug: open-benchling-locations-api
- collection_type: open
  name: Benchling AA Sequences Mixtures API
  slug: open-benchling-mixtures-api
- collection_type: open
  name: Benchling AA Sequences Molecules API
  slug: open-benchling-molecules-api
- collection_type: open
  name: Benchling AA Sequences Monomers API
  slug: open-benchling-monomers-api
- collection_type: open
  name: Benchling AA Sequences Nucleotide Alignments API
  slug: open-benchling-nucleotide-alignments-api
- collection_type: open
  name: Benchling AA Sequences Oligos API
  slug: open-benchling-oligos-api
- collection_type: open
  name: Benchling AA Sequences Organizations API
  slug: open-benchling-organizations-api
- collection_type: open
  name: Benchling AA Sequences Plates API
  slug: open-benchling-plates-api
- collection_type: open
  name: Benchling AA Sequences Printers API
  slug: open-benchling-printers-api
- collection_type: open
  name: Benchling AA Sequences Projects API
  slug: open-benchling-projects-api
- collection_type: open
  name: Benchling AA Sequences Registry API
  slug: open-benchling-registry-api
- collection_type: open
  name: Benchling AA Sequences RNA Oligos API
  slug: open-benchling-rna-oligos-api
- collection_type: open
  name: Benchling AA Sequences RNA Sequences API
  slug: open-benchling-rna-sequences-api
- collection_type: open
  name: Benchling AA Sequences Schemas API
  slug: open-benchling-schemas-api
- collection_type: open
  name: Benchling AA Sequences Tasks API
  slug: open-benchling-tasks-api
- collection_type: open
  name: Benchling AA Sequences Teams API
  slug: open-benchling-teams-api
- collection_type: open
  name: Benchling AA Sequences Users API
  slug: open-benchling-users-api
- collection_type: open
  name: Benchling AA Sequences Warehouse API
  slug: open-benchling-warehouse-api
- collection_type: open
  name: Benchling AA Sequences Workflow Flowchart Config Versions API
  slug: open-benchling-workflow-flowchart-config-versions-api
- collection_type: open
  name: Benchling AA Sequences Workflow Flowcharts API
  slug: open-benchling-workflow-flowcharts-api
- collection_type: open
  name: Benchling AA Sequences Workflow Outputs API
  slug: open-benchling-workflow-outputs-api
- collection_type: open
  name: Benchling AA Sequences Workflow Task Groups API
  slug: open-benchling-workflow-task-groups-api
- collection_type: open
  name: Benchling AA Sequences Workflow Tasks API
  slug: open-benchling-workflow-tasks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/benchling-capability-edges.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/benchling-v3-openapi.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/benchling-v3-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/benchling-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/benchling-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/benchling-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/benchling-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/benchling-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/benchling-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/benchling-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/benchling-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/benchling-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/benchling-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/benchling-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/benchling-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/benchling-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/benchling-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/benchling-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.benchling.com/developer-platform
- group: docs
  title: ''
  type: APIReference
  url: https://benchling.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.benchling.com/docs/getting-started-benchling-apps
- group: operate
  title: ''
  type: Support
  url: https://help.benchling.com/hc/en-us/requests/new
- group: commercial
  title: ''
  type: Pricing
  url: https://www.benchling.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://benchling.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.benchling.com/agreements-and-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.benchling.com/privacy
- group: operate
  title: ''
  type: Community
  url: https://community.benchling.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/benchling-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benchling-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/benchling-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/benchling-scopes.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.benchling.com/docs/developer-platform-overview
- group: docs
  title: ''
  type: Reference
  url: https://benchling.com/api/reference
- group: auth
  title: ''
  type: Authentication
  url: https://docs.benchling.com/docs/getting-started-benchling-apps
- group: build
  title: ''
  type: SDKs
  url: https://docs.benchling.com/docs/getting-started-with-the-sdk
- group: build
  title: ''
  type: SDKPython
  url: https://pypi.org/project/benchling-sdk/
- group: design
  title: ''
  type: Webhooks
  url: https://docs.benchling.com/docs/getting-started-with-webhooks
- group: docs
  title: ''
  type: WebhookReference
  url: https://benchling.com/webhooks/reference
- group: other
  title: ''
  type: Events
  url: https://docs.benchling.com/docs/events-getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.benchling.com/changelog
- group: operate
  title: ''
  type: DeveloperChangelog
  url: https://docs.benchling.com/changelog/benchling-developer-changelog
- group: company
  title: ''
  type: Blog
  url: https://www.benchling.com/blog
- group: operate
  title: ''
  type: Status
  url: https://benchling.betteruptime.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benchling
- group: other
  title: ''
  type: DeveloperPlatform
  url: https://www.benchling.com/developer-platform
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.benchling.com/docs/rate-limiting
- group: commercial
  title: ''
  type: Plans
  url: plans/benchling-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/benchling-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/benchling-finops.yml
created: 2026-06-13
description: Benchling is a life sciences R&D cloud platform offering a comprehensive REST API for programmatically managing molecular biology entities, assay results and runs, electronic lab notebook entries, DNA/RNA/protein sequences, inventory, and experiment workflows. The API enables integrations with lab instruments, ERP systems, LIMS, and external databases, as well as bulk data ingest/export and event-driven automation via webhooks and AWS EventBridge. API access is available to Professional and Enterprise tenants and supports user API keys, OAuth 2.0 client credentials, and OIDC authentication.
examples:
- key_count: 5
  name: Createappconfigurationitem Request
  slug: createAppConfigurationItem-request
- key_count: 6
  name: Createappconfigurationitem Response 201
  slug: createAppConfigurationItem-response-201
- key_count: 5
  name: Createblob Request
  slug: createBlob-request
- key_count: 6
  name: Createdataframe Response 200
  slug: createDataFrame-response-200
- key_count: 6
  name: Createfile Response 200
  slug: createFile-response-200
- key_count: 6
  name: Getappconfigurationitembyid Response 200
  slug: getAppConfigurationItemById-response-200
- key_count: 6
  name: Getdataframe Response 200
  slug: getDataFrame-response-200
- key_count: 6
  name: Gettask Response 200
  slug: getTask-response-200
- key_count: 6
  name: Patchdataframe Response 202
  slug: patchDataFrame-response-202
- key_count: 5
  name: Updateappconfigurationitem Request
  slug: updateAppConfigurationItem-request
finops:
- name: Benchling Finops
  service_category: ''
  slug: benchling-finops
graphqls:
- description: Benchling is a life sciences R&D cloud platform for biotech and pharma. The API covers notebook entries, sequences, molecules, assay results, registration, inventory management, plates, workflows, and
  name: Benchling GraphQL API
  slug: benchling-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/benchling.png
json_schemas:
- name: AIGGenerateInputAsyncTask
  property_count: 0
  slug: AIGGenerateInputAsyncTask
- name: AOPProcessOutputAsyncTask
  property_count: 0
  slug: AOPProcessOutputAsyncTask
- name: AaAnnotation
  property_count: 7
  slug: AaAnnotation
- name: AaSequence
  property_count: 21
  slug: AaSequence
- name: AaSequenceBaseRequest
  property_count: 9
  slug: AaSequenceBaseRequest
- name: AaSequenceBaseRequestForCreate
  property_count: 0
  slug: AaSequenceBaseRequestForCreate
- name: AaSequenceBulkCreate
  property_count: 0
  slug: AaSequenceBulkCreate
- name: AaSequenceBulkUpdate
  property_count: 0
  slug: AaSequenceBulkUpdate
- name: AaSequenceBulkUpsertRequest
  property_count: 0
  slug: AaSequenceBulkUpsertRequest
- name: AaSequenceCreate
  property_count: 0
  slug: AaSequenceCreate
- name: AaSequenceRequestRegistryFields
  property_count: 1
  slug: AaSequenceRequestRegistryFields
- name: AaSequenceSummary
  property_count: 3
  slug: AaSequenceSummary
- name: AaSequenceUpdate
  property_count: 0
  slug: AaSequenceUpdate
- name: AaSequenceUpsert
  property_count: 0
  slug: AaSequenceUpsert
- name: AaSequenceWithEntityType
  property_count: 0
  slug: AaSequenceWithEntityType
- name: AaSequencesArchivalChange
  property_count: 2
  slug: AaSequencesArchivalChange
- name: AaSequencesArchive
  property_count: 2
  slug: AaSequencesArchive
- name: AaSequencesBulkCreateRequest
  property_count: 1
  slug: AaSequencesBulkCreateRequest
- name: AaSequencesBulkGet
  property_count: 1
  slug: AaSequencesBulkGet
- name: AaSequencesBulkUpdateRequest
  property_count: 1
  slug: AaSequencesBulkUpdateRequest
- name: AaSequencesBulkUpsertRequest
  property_count: 1
  slug: AaSequencesBulkUpsertRequest
- name: AaSequencesFindMatchingRegion
  property_count: 3
  slug: AaSequencesFindMatchingRegion
- name: AaSequencesMatchBases
  property_count: 6
  slug: AaSequencesMatchBases
- name: AaSequencesPaginatedList
  property_count: 2
  slug: AaSequencesPaginatedList
- name: AaSequencesSearchBases
  property_count: 6
  slug: AaSequencesSearchBases
- name: AaSequencesUnarchive
  property_count: 1
  slug: AaSequencesUnarchive
- name: AlignedNucleotideSequence
  property_count: 7
  slug: AlignedNucleotideSequence
- name: AlignedSequence
  property_count: 7
  slug: AlignedSequence
- name: AppCanvas
  property_count: 0
  slug: AppCanvas
- name: AppCanvasBase
  property_count: 0
  slug: AppCanvasBase
- name: AppCanvasCreate
  property_count: 0
  slug: AppCanvasCreate
- name: AppCanvasCreateBase
  property_count: 0
  slug: AppCanvasCreateBase
- name: AppCanvasCreateUiBlockList
  property_count: 1
  slug: AppCanvasCreateUiBlockList
- name: AppCanvasLeafNodeUiBlockList
  property_count: 1
  slug: AppCanvasLeafNodeUiBlockList
- name: AppCanvasNotePart
  property_count: 0
  slug: AppCanvasNotePart
- name: AppCanvasUiBlockList
  property_count: 1
  slug: AppCanvasUiBlockList
- name: AppCanvasUpdate
  property_count: 0
  slug: AppCanvasUpdate
- name: AppCanvasUpdateBase
  property_count: 0
  slug: AppCanvasUpdateBase
- name: AppCanvasUpdateUiBlockList
  property_count: 1
  slug: AppCanvasUpdateUiBlockList
- name: AppCanvasWriteBase
  property_count: 0
  slug: AppCanvasWriteBase
- name: AppCanvasesArchivalChange
  property_count: 1
  slug: AppCanvasesArchivalChange
- name: AppCanvasesArchive
  property_count: 2
  slug: AppCanvasesArchive
- name: AppCanvasesArchiveReason
  property_count: 0
  slug: AppCanvasesArchiveReason
- name: AppCanvasesUnarchive
  property_count: 1
  slug: AppCanvasesUnarchive
- name: AppConfigItem
  property_count: 0
  slug: AppConfigItem
- name: AppConfigItemApiMixin
  property_count: 7
  slug: AppConfigItemApiMixin
- name: AppConfigItemBooleanBulkUpdate
  property_count: 0
  slug: AppConfigItemBooleanBulkUpdate
- name: AppConfigItemBooleanCreate
  property_count: 0
  slug: AppConfigItemBooleanCreate
- name: AppConfigItemBooleanUpdate
  property_count: 2
  slug: AppConfigItemBooleanUpdate
- name: AppConfigItemBulkUpdate
  property_count: 0
  slug: AppConfigItemBulkUpdate
- name: AppConfigItemBulkUpdateMixin
  property_count: 1
  slug: AppConfigItemBulkUpdateMixin
- name: AppConfigItemCreate
  property_count: 0
  slug: AppConfigItemCreate
- name: AppConfigItemCreateMixin
  property_count: 2
  slug: AppConfigItemCreateMixin
- name: AppConfigItemDateBulkUpdate
  property_count: 0
  slug: AppConfigItemDateBulkUpdate
- name: AppConfigItemDateCreate
  property_count: 0
  slug: AppConfigItemDateCreate
- name: AppConfigItemDateUpdate
  property_count: 2
  slug: AppConfigItemDateUpdate
- name: AppConfigItemDatetimeBulkUpdate
  property_count: 0
  slug: AppConfigItemDatetimeBulkUpdate
- name: AppConfigItemDatetimeCreate
  property_count: 0
  slug: AppConfigItemDatetimeCreate
- name: AppConfigItemDatetimeUpdate
  property_count: 2
  slug: AppConfigItemDatetimeUpdate
- name: AppConfigItemFloatBulkUpdate
  property_count: 0
  slug: AppConfigItemFloatBulkUpdate
- name: AppConfigItemFloatCreate
  property_count: 0
  slug: AppConfigItemFloatCreate
- name: AppConfigItemFloatUpdate
  property_count: 2
  slug: AppConfigItemFloatUpdate
- name: AppConfigItemGenericBulkUpdate
  property_count: 0
  slug: AppConfigItemGenericBulkUpdate
- name: AppConfigItemGenericCreate
  property_count: 0
  slug: AppConfigItemGenericCreate
- name: AppConfigItemGenericUpdate
  property_count: 2
  slug: AppConfigItemGenericUpdate
- name: AppConfigItemIntegerBulkUpdate
  property_count: 0
  slug: AppConfigItemIntegerBulkUpdate
- name: AppConfigItemIntegerCreate
  property_count: 0
  slug: AppConfigItemIntegerCreate
- name: AppConfigItemIntegerUpdate
  property_count: 2
  slug: AppConfigItemIntegerUpdate
- name: AppConfigItemJsonBulkUpdate
  property_count: 0
  slug: AppConfigItemJsonBulkUpdate
- name: AppConfigItemJsonCreate
  property_count: 0
  slug: AppConfigItemJsonCreate
- name: AppConfigItemJsonUpdate
  property_count: 2
  slug: AppConfigItemJsonUpdate
- name: AppConfigItemUpdate
  property_count: 0
  slug: AppConfigItemUpdate
- name: AppConfigItemsBulkCreateRequest
  property_count: 1
  slug: AppConfigItemsBulkCreateRequest
- name: AppConfigItemsBulkUpdateRequest
  property_count: 1
  slug: AppConfigItemsBulkUpdateRequest
- name: AppConfigurationPaginatedList
  property_count: 0
  slug: AppConfigurationPaginatedList
- name: AppSession
  property_count: 8
  slug: AppSession
- name: AppSessionCreate
  property_count: 4
  slug: AppSessionCreate
- name: AppSessionMessage
  property_count: 0
  slug: AppSessionMessage
- name: AppSessionMessageCreate
  property_count: 2
  slug: AppSessionMessageCreate
- name: AppSessionMessageStyle
  property_count: 0
  slug: AppSessionMessageStyle
- name: AppSessionStatus
  property_count: 0
  slug: AppSessionStatus
- name: AppSessionUpdate
  property_count: 3
  slug: AppSessionUpdate
- name: AppSessionUpdateStatus
  property_count: 0
  slug: AppSessionUpdateStatus
- name: AppSummary
  property_count: 1
  slug: AppSummary
- name: ArchiveRecord
  property_count: 1
  slug: ArchiveRecord
- name: ArchiveRecordSet
  property_count: 0
  slug: ArchiveRecordSet
- name: ArrayElementAppConfigItem
  property_count: 0
  slug: ArrayElementAppConfigItem
- name: AssayFieldsCreate
  property_count: 0
  slug: AssayFieldsCreate
- name: AssayResult
  property_count: 14
  slug: AssayResult
- name: AssayResultCreate
  property_count: 5
  slug: AssayResultCreate
- name: AssayResultIdsRequest
  property_count: 1
  slug: AssayResultIdsRequest
- name: AssayResultIdsResponse
  property_count: 1
  slug: AssayResultIdsResponse
- name: AssayResultSchema
  property_count: 0
  slug: AssayResultSchema
- name: AssayResultSchemasPaginatedList
  property_count: 2
  slug: AssayResultSchemasPaginatedList
- name: AssayResultTransactionCreateResponse
  property_count: 1
  slug: AssayResultTransactionCreateResponse
- name: AssayResultsArchive
  property_count: 0
  slug: AssayResultsArchive
- name: AssayResultsBulkCreateInTableRequest
  property_count: 0
  slug: AssayResultsBulkCreateInTableRequest
- name: AssayResultsBulkCreateRequest
  property_count: 1
  slug: AssayResultsBulkCreateRequest
- name: AssayResultsBulkGet
  property_count: 1
  slug: AssayResultsBulkGet
- name: AssayResultsCreateErrorResponse
  property_count: 2
  slug: AssayResultsCreateErrorResponse
- name: AssayResultsCreateResponse
  property_count: 2
  slug: AssayResultsCreateResponse
- name: AssayResultsPaginatedList
  property_count: 2
  slug: AssayResultsPaginatedList
- name: AssayRun
  property_count: 14
  slug: AssayRun
- name: AssayRunCreate
  property_count: 6
  slug: AssayRunCreate
- name: AssayRunCreatedEvent
  property_count: 0
  slug: AssayRunCreatedEvent
- name: AssayRunNotePart
  property_count: 0
  slug: AssayRunNotePart
- name: AssayRunSchema
  property_count: 0
  slug: AssayRunSchema
- name: AssayRunSchemasPaginatedList
  property_count: 2
  slug: AssayRunSchemasPaginatedList
- name: AssayRunUpdate
  property_count: 2
  slug: AssayRunUpdate
- name: AssayRunUpdatedFieldsEvent
  property_count: 0
  slug: AssayRunUpdatedFieldsEvent
- name: AssayRunValidationStatus
  property_count: 0
  slug: AssayRunValidationStatus
- name: AssayRunsArchivalChange
  property_count: 1
  slug: AssayRunsArchivalChange
- name: AssayRunsArchive
  property_count: 2
  slug: AssayRunsArchive
- name: AssayRunsBulkCreateErrorResponse
  property_count: 2
  slug: AssayRunsBulkCreateErrorResponse
- name: AssayRunsBulkCreateRequest
  property_count: 1
  slug: AssayRunsBulkCreateRequest
- name: AssayRunsBulkCreateResponse
  property_count: 2
  slug: AssayRunsBulkCreateResponse
- name: AssayRunsBulkGet
  property_count: 1
  slug: AssayRunsBulkGet
- name: AssayRunsPaginatedList
  property_count: 2
  slug: AssayRunsPaginatedList
- name: AssayRunsUnarchive
  property_count: 1
  slug: AssayRunsUnarchive
- name: AsyncTask
  property_count: 4
  slug: AsyncTask
- name: AsyncTaskLink
  property_count: 1
  slug: AsyncTaskLink
- name: AuditLogExport
  property_count: 1
  slug: AuditLogExport
- name: AutoAnnotateAaSequences
  property_count: 2
  slug: AutoAnnotateAaSequences
- name: AutoAnnotateDnaSequences
  property_count: 2
  slug: AutoAnnotateDnaSequences
- name: AutoAnnotateRnaSequences
  property_count: 2
  slug: AutoAnnotateRnaSequences
- name: AutofillPartsAsyncTask
  property_count: 0
  slug: AutofillPartsAsyncTask
- name: AutofillRnaSequences
  property_count: 1
  slug: AutofillRnaSequences
- name: AutofillSequences
  property_count: 1
  slug: AutofillSequences
- name: AutofillTranscriptionsAsyncTask
  property_count: 0
  slug: AutofillTranscriptionsAsyncTask
- name: AutofillTranslationsAsyncTask
  property_count: 0
  slug: AutofillTranslationsAsyncTask
- name: AutomationFile
  property_count: 5
  slug: AutomationFile
- name: AutomationFileInputsPaginatedList
  property_count: 2
  slug: AutomationFileInputsPaginatedList
- name: AutomationInputGenerator
  property_count: 0
  slug: AutomationInputGenerator
- name: AutomationInputGeneratorCompletedV2BetaEvent
  property_count: 0
  slug: AutomationInputGeneratorCompletedV2BetaEvent
- name: AutomationInputGeneratorCompletedV2Event
  property_count: 0
  slug: AutomationInputGeneratorCompletedV2Event
- name: AutomationInputGeneratorUpdate
  property_count: 1
  slug: AutomationInputGeneratorUpdate
- name: AutomationOutputProcessor
  property_count: 0
  slug: AutomationOutputProcessor
- name: AutomationOutputProcessorArchivalChange
  property_count: 2
  slug: AutomationOutputProcessorArchivalChange
- name: AutomationOutputProcessorCompletedV2BetaEvent
  property_count: 0
  slug: AutomationOutputProcessorCompletedV2BetaEvent
- name: AutomationOutputProcessorCompletedV2Event
  property_count: 0
  slug: AutomationOutputProcessorCompletedV2Event
- name: AutomationOutputProcessorCreate
  property_count: 7
  slug: AutomationOutputProcessorCreate
- name: AutomationOutputProcessorUpdate
  property_count: 1
  slug: AutomationOutputProcessorUpdate
- name: AutomationOutputProcessorUploadedV2BetaEvent
  property_count: 0
  slug: AutomationOutputProcessorUploadedV2BetaEvent
- name: AutomationOutputProcessorUploadedV2Event
  property_count: 0
  slug: AutomationOutputProcessorUploadedV2Event
- name: AutomationOutputProcessorsArchive
  property_count: 2
  slug: AutomationOutputProcessorsArchive
- name: AutomationOutputProcessorsPaginatedList
  property_count: 2
  slug: AutomationOutputProcessorsPaginatedList
- name: AutomationOutputProcessorsUnarchive
  property_count: 1
  slug: AutomationOutputProcessorsUnarchive
- name: AutomationProgressStats
  property_count: 3
  slug: AutomationProgressStats
- name: AutomationTransformStatusFailedEventV2Event
  property_count: 0
  slug: AutomationTransformStatusFailedEventV2Event
- name: AutomationTransformStatusPendingEventV2Event
  property_count: 0
  slug: AutomationTransformStatusPendingEventV2Event
- name: AutomationTransformStatusRunningEventV2Event
  property_count: 0
  slug: AutomationTransformStatusRunningEventV2Event
- name: AutomationTransformStatusSucceededEventV2Event
  property_count: 0
  slug: AutomationTransformStatusSucceededEventV2Event
- name: BackTranslate
  property_count: 11
  slug: BackTranslate
- name: BadRequestError
  property_count: 1
  slug: BadRequestError
- name: BadRequestErrorBulk
  property_count: 0
  slug: BadRequestErrorBulk
- name: BarcodeValidationResult
  property_count: 3
  slug: BarcodeValidationResult
- name: BarcodeValidationResults
  property_count: 1
  slug: BarcodeValidationResults
- name: BarcodesList
  property_count: 1
  slug: BarcodesList
- name: BaseAppConfigItem
  property_count: 0
  slug: BaseAppConfigItem
- name: BaseAssaySchema
  property_count: 0
  slug: BaseAssaySchema
- name: BaseDropdownUIBlock
  property_count: 0
  slug: BaseDropdownUIBlock
- name: BaseError
  property_count: 3
  slug: BaseError
- name: BaseNotePart
  property_count: 2
  slug: BaseNotePart
- name: BaseSearchInputUIBlock
  property_count: 0
  slug: BaseSearchInputUIBlock
- name: BaseSelectorInputUIBlock
  property_count: 0
  slug: BaseSelectorInputUIBlock
- name: Batch
  property_count: 11
  slug: Batch
- name: BatchOrInaccessibleResource
  property_count: 0
  slug: BatchOrInaccessibleResource
- name: BatchSchema
  property_count: 0
  slug: BatchSchema
- name: BatchSchemasList
  property_count: 1
  slug: BatchSchemasList
- name: BatchSchemasPaginatedList
  property_count: 0
  slug: BatchSchemasPaginatedList
- name: BenchlingApp
  property_count: 0
  slug: BenchlingApp
- name: BenchlingAppCreate
  property_count: 2
  slug: BenchlingAppCreate
- name: BenchlingAppUpdate
  property_count: 2
  slug: BenchlingAppUpdate
- name: BenchlingAppsArchivalChange
  property_count: 1
  slug: BenchlingAppsArchivalChange
- name: BenchlingAppsArchive
  property_count: 2
  slug: BenchlingAppsArchive
- name: BenchlingAppsPaginatedList
  property_count: 0
  slug: BenchlingAppsPaginatedList
- name: BenchlingAppsUnarchive
  property_count: 1
  slug: BenchlingAppsUnarchive
- name: Blob
  property_count: 5
  slug: Blob
- name: BlobComplete
  property_count: 1
  slug: BlobComplete
- name: BlobCreate
  property_count: 5
  slug: BlobCreate
- name: BlobMultipartCreate
  property_count: 3
  slug: BlobMultipartCreate
- name: BlobPart
  property_count: 2
  slug: BlobPart
- name: BlobPartCreate
  property_count: 3
  slug: BlobPartCreate
- name: BlobUrl
  property_count: 2
  slug: BlobUrl
- name: BlobsBulkGet
  property_count: 1
  slug: BlobsBulkGet
- name: BooleanAppConfigItem
  property_count: 0
  slug: BooleanAppConfigItem
- name: Box
  property_count: 19
  slug: Box
- name: BoxContentsPaginatedList
  property_count: 2
  slug: BoxContentsPaginatedList
- name: BoxCreate
  property_count: 6
  slug: BoxCreate
- name: BoxCreationTableNotePart
  property_count: 0
  slug: BoxCreationTableNotePart
- name: BoxSchema
  property_count: 0
  slug: BoxSchema
- name: BoxSchemasList
  property_count: 1
  slug: BoxSchemasList
- name: BoxSchemasPaginatedList
  property_count: 0
  slug: BoxSchemasPaginatedList
- name: BoxUpdate
  property_count: 4
  slug: BoxUpdate
- name: BoxesArchivalChange
  property_count: 2
  slug: BoxesArchivalChange
- name: BoxesArchive
  property_count: 3
  slug: BoxesArchive
- name: BoxesBulkGet
  property_count: 1
  slug: BoxesBulkGet
- name: BoxesPaginatedList
  property_count: 2
  slug: BoxesPaginatedList
- name: BoxesUnarchive
  property_count: 1
  slug: BoxesUnarchive
- name: BulkCreateAaSequencesAsyncTask
  property_count: 0
  slug: BulkCreateAaSequencesAsyncTask
- name: BulkCreateContainersAsyncTask
  property_count: 0
  slug: BulkCreateContainersAsyncTask
- name: BulkCreateCustomEntitiesAsyncTask
  property_count: 0
  slug: BulkCreateCustomEntitiesAsyncTask
- name: BulkCreateDnaOligosAsyncTask
  property_count: 0
  slug: BulkCreateDnaOligosAsyncTask
- name: BulkCreateDnaSequencesAsyncTask
  property_count: 0
  slug: BulkCreateDnaSequencesAsyncTask
- name: BulkCreateFeaturesAsyncTask
  property_count: 0
  slug: BulkCreateFeaturesAsyncTask
- name: BulkCreateRnaOligosAsyncTask
  property_count: 0
  slug: BulkCreateRnaOligosAsyncTask
- name: BulkCreateRnaSequencesAsyncTask
  property_count: 0
  slug: BulkCreateRnaSequencesAsyncTask
- name: BulkRegisterEntitiesAsyncTask
  property_count: 0
  slug: BulkRegisterEntitiesAsyncTask
- name: BulkUpdateAaSequencesAsyncTask
  property_count: 0
  slug: BulkUpdateAaSequencesAsyncTask
- name: BulkUpdateContainersAsyncTask
  property_count: 0
  slug: BulkUpdateContainersAsyncTask
- name: BulkUpdateCustomEntitiesAsyncTask
  property_count: 0
  slug: BulkUpdateCustomEntitiesAsyncTask
- name: BulkUpdateDnaOligosAsyncTask
  property_count: 0
  slug: BulkUpdateDnaOligosAsyncTask
- name: BulkUpdateDnaSequencesAsyncTask
  property_count: 0
  slug: BulkUpdateDnaSequencesAsyncTask
- name: BulkUpdateRnaOligosAsyncTask
  property_count: 0
  slug: BulkUpdateRnaOligosAsyncTask
- name: BulkUpdateRnaSequencesAsyncTask
  property_count: 0
  slug: BulkUpdateRnaSequencesAsyncTask
- name: ButtonUiBlock
  property_count: 0
  slug: ButtonUiBlock
- name: ButtonUiBlockCreate
  property_count: 0
  slug: ButtonUiBlockCreate
- name: ButtonUiBlockUpdate
  property_count: 0
  slug: ButtonUiBlockUpdate
- name: ChartNotePart
  property_count: 0
  slug: ChartNotePart
- name: CheckboxNotePart
  property_count: 0
  slug: CheckboxNotePart
- name: CheckoutRecord
  property_count: 4
  slug: CheckoutRecord
- name: ChipUiBlock
  property_count: 0
  slug: ChipUiBlock
- name: ChipUiBlockCreate
  property_count: 0
  slug: ChipUiBlockCreate
- name: ChipUiBlockUpdate
  property_count: 0
  slug: ChipUiBlockUpdate
- name: ClustaloOptions
  property_count: 5
  slug: ClustaloOptions
- name: CodonUsageTable
  property_count: 2
  slug: CodonUsageTable
- name: CodonUsageTablesPaginatedList
  property_count: 0
  slug: CodonUsageTablesPaginatedList
- name: ConflictError
  property_count: 1
  slug: ConflictError
- name: Container
  property_count: 21
  slug: Container
- name: ContainerBulkUpdateItem
  property_count: 0
  slug: ContainerBulkUpdateItem
- name: ContainerContent
  property_count: 3
  slug: ContainerContent
- name: ContainerContentUpdate
  property_count: 1
  slug: ContainerContentUpdate
- name: ContainerContentsList
  property_count: 1
  slug: ContainerContentsList
- name: ContainerCreate
  property_count: 0
  slug: ContainerCreate
- name: ContainerLabels
  property_count: 3
  slug: ContainerLabels
- name: ContainerQuantity
  property_count: 2
  slug: ContainerQuantity
- name: ContainerSchema
  property_count: 0
  slug: ContainerSchema
- name: ContainerSchemasList
  property_count: 1
  slug: ContainerSchemasList
- name: ContainerSchemasPaginatedList
  property_count: 0
  slug: ContainerSchemasPaginatedList
- name: ContainerTransfer
  property_count: 0
  slug: ContainerTransfer
- name: ContainerTransferBase
  property_count: 8
  slug: ContainerTransferBase
- name: ContainerTransferDestinationContentsItem
  property_count: 2
  slug: ContainerTransferDestinationContentsItem
- name: ContainerUpdate
  property_count: 0
  slug: ContainerUpdate
- name: ContainerWithCoordinates
  property_count: 0
  slug: ContainerWithCoordinates
- name: ContainerWriteBase
  property_count: 6
  slug: ContainerWriteBase
- name: ContainersArchivalChange
  property_count: 1
  slug: ContainersArchivalChange
- name: ContainersArchive
  property_count: 3
  slug: ContainersArchive
- name: ContainersBulkCreateRequest
  property_count: 1
  slug: ContainersBulkCreateRequest
- name: ContainersBulkUpdateRequest
  property_count: 1
  slug: ContainersBulkUpdateRequest
- name: ContainersCheckin
  property_count: 2
  slug: ContainersCheckin
- name: ContainersCheckout
  property_count: 3
  slug: ContainersCheckout
- name: ContainersList
  property_count: 1
  slug: ContainersList
- name: ContainersPaginatedList
  property_count: 0
  slug: ContainersPaginatedList
- name: ContainersUnarchive
  property_count: 1
  slug: ContainersUnarchive
- name: ConvertToASM
  property_count: 3
  slug: ConvertToASM
- name: ConvertToCSV
  property_count: 6
  slug: ConvertToCSV
- name: CreateConsensusAlignmentAsyncTask
  property_count: 0
  slug: CreateConsensusAlignmentAsyncTask
- name: CreateEntityIntoRegistry
  property_count: 4
  slug: CreateEntityIntoRegistry
- name: CreateNucleotideConsensusAlignmentAsyncTask
  property_count: 0
  slug: CreateNucleotideConsensusAlignmentAsyncTask
- name: CreateNucleotideTemplateAlignmentAsyncTask
  property_count: 0
  slug: CreateNucleotideTemplateAlignmentAsyncTask
- name: CreateTemplateAlignmentAsyncTask
  property_count: 0
  slug: CreateTemplateAlignmentAsyncTask
- name: CreationOrigin
  property_count: 4
  slug: CreationOrigin
- name: CustomEntitiesArchivalChange
  property_count: 2
  slug: CustomEntitiesArchivalChange
- name: CustomEntitiesArchive
  property_count: 2
  slug: CustomEntitiesArchive
- name: CustomEntitiesBulkCreateRequest
  property_count: 1
  slug: CustomEntitiesBulkCreateRequest
- name: CustomEntitiesBulkUpdateRequest
  property_count: 1
  slug: CustomEntitiesBulkUpdateRequest
- name: CustomEntitiesBulkUpsertRequest
  property_count: 1
  slug: CustomEntitiesBulkUpsertRequest
- name: CustomEntitiesList
  property_count: 1
  slug: CustomEntitiesList
- name: CustomEntitiesPaginatedList
  property_count: 2
  slug: CustomEntitiesPaginatedList
- name: CustomEntitiesUnarchive
  property_count: 1
  slug: CustomEntitiesUnarchive
- name: CustomEntity
  property_count: 18
  slug: CustomEntity
- name: CustomEntityBaseRequest
  property_count: 7
  slug: CustomEntityBaseRequest
- name: CustomEntityBaseRequestForCreate
  property_count: 0
  slug: CustomEntityBaseRequestForCreate
- name: CustomEntityBulkCreate
  property_count: 0
  slug: CustomEntityBulkCreate
- name: CustomEntityBulkUpdate
  property_count: 1
  slug: CustomEntityBulkUpdate
- name: CustomEntityBulkUpsertRequest
  property_count: 0
  slug: CustomEntityBulkUpsertRequest
- name: CustomEntityCreate
  property_count: 0
  slug: CustomEntityCreate
- name: CustomEntityRequestRegistryFields
  property_count: 1
  slug: CustomEntityRequestRegistryFields
- name: CustomEntitySummary
  property_count: 3
  slug: CustomEntitySummary
- name: CustomEntityUpdate
  property_count: 0
  slug: CustomEntityUpdate
- name: CustomEntityUpsertRequest
  property_count: 0
  slug: CustomEntityUpsertRequest
- name: CustomEntityWithEntityType
  property_count: 0
  slug: CustomEntityWithEntityType
- name: CustomField
  property_count: 1
  slug: CustomField
- name: CustomFields
  property_count: 0
  slug: CustomFields
- name: CustomNotation
  property_count: 3
  slug: CustomNotation
- name: CustomNotationAlias
  property_count: 9
  slug: CustomNotationAlias
- name: CustomNotationRequest
  property_count: 2
  slug: CustomNotationRequest
- name: CustomNotationsPaginatedList
  property_count: 0
  slug: CustomNotationsPaginatedList
- name: DataFrame
  property_count: 0
  slug: DataFrame
- name: DataFrameColumnMetadata
  property_count: 2
  slug: DataFrameColumnMetadata
- name: DataFrameColumnTypeMetadata
  property_count: 0
  slug: DataFrameColumnTypeMetadata
- name: DataFrameColumnTypeNameEnum
  property_count: 1
  slug: DataFrameColumnTypeNameEnum
- name: DataFrameCreate
  property_count: 0
  slug: DataFrameCreate
- name: DataFrameCreateManifest
  property_count: 1
  slug: DataFrameCreateManifest
- name: DataFrameManifest
  property_count: 1
  slug: DataFrameManifest
- name: DataFrameUpdate
  property_count: 1
  slug: DataFrameUpdate
- name: Dataset
  property_count: 0
  slug: Dataset
- name: DatasetCreate
  property_count: 5
  slug: DatasetCreate
- name: DatasetUpdate
  property_count: 3
  slug: DatasetUpdate
- name: DatasetsArchivalChange
  property_count: 1
  slug: DatasetsArchivalChange
- name: DatasetsArchive
  property_count: 2
  slug: DatasetsArchive
- name: DatasetsPaginatedList
  property_count: 2
  slug: DatasetsPaginatedList
- name: DatasetsUnarchive
  property_count: 1
  slug: DatasetsUnarchive
- name: DateAppConfigItem
  property_count: 0
  slug: DateAppConfigItem
- name: DatetimeAppConfigItem
  property_count: 0
  slug: DatetimeAppConfigItem
- name: DeprecatedAutomationOutputProcessorsPaginatedList
  property_count: 2
  slug: DeprecatedAutomationOutputProcessorsPaginatedList
- name: DeprecatedContainerVolumeForInput
  property_count: 2
  slug: DeprecatedContainerVolumeForInput
- name: DeprecatedContainerVolumeForResponse
  property_count: 0
  slug: DeprecatedContainerVolumeForResponse
- name: DeprecatedEntitySchema
  property_count: 0
  slug: DeprecatedEntitySchema
- name: DeprecatedEntitySchemasList
  property_count: 1
  slug: DeprecatedEntitySchemasList
- name: DnaAlignment
  property_count: 0
  slug: DnaAlignment
- name: DnaAlignmentBase
  property_count: 5
  slug: DnaAlignmentBase
- name: DnaAlignmentSummary
  property_count: 7
  slug: DnaAlignmentSummary
- name: DnaAlignmentsPaginatedList
  property_count: 0
  slug: DnaAlignmentsPaginatedList
- name: DnaAnnotation
  property_count: 0
  slug: DnaAnnotation
- name: DnaConsensusAlignmentCreate
  property_count: 0
  slug: DnaConsensusAlignmentCreate
- name: DnaOligo
  property_count: 0
  slug: DnaOligo
- name: DnaOligoBulkUpdate
  property_count: 0
  slug: DnaOligoBulkUpdate
- name: DnaOligoCreate
  property_count: 0
  slug: DnaOligoCreate
- name: DnaOligoUpdate
  property_count: 0
  slug: DnaOligoUpdate
- name: DnaOligoWithEntityType
  property_count: 0
  slug: DnaOligoWithEntityType
- name: DnaOligosArchivalChange
  property_count: 2
  slug: DnaOligosArchivalChange
- name: DnaOligosArchive
  property_count: 2
  slug: DnaOligosArchive
- name: DnaOligosBulkCreateRequest
  property_count: 1
  slug: DnaOligosBulkCreateRequest
- name: DnaOligosBulkUpdateRequest
  property_count: 1
  slug: DnaOligosBulkUpdateRequest
- name: DnaOligosBulkUpsertRequest
  property_count: 1
  slug: DnaOligosBulkUpsertRequest
- name: DnaOligosPaginatedList
  property_count: 0
  slug: DnaOligosPaginatedList
- name: DnaOligosUnarchive
  property_count: 1
  slug: DnaOligosUnarchive
- name: DnaSequence
  property_count: 27
  slug: DnaSequence
- name: DnaSequenceBaseRequest
  property_count: 13
  slug: DnaSequenceBaseRequest
- name: DnaSequenceBaseRequestForCreate
  property_count: 0
  slug: DnaSequenceBaseRequestForCreate
- name: DnaSequenceBulkCreate
  property_count: 0
  slug: DnaSequenceBulkCreate
- name: DnaSequenceBulkUpdate
  property_count: 0
  slug: DnaSequenceBulkUpdate
- name: DnaSequenceBulkUpsertRequest
  property_count: 0
  slug: DnaSequenceBulkUpsertRequest
- name: DnaSequenceCreate
  property_count: 0
  slug: DnaSequenceCreate
- name: DnaSequencePart
  property_count: 0
  slug: DnaSequencePart
- name: DnaSequenceRequestRegistryFields
  property_count: 1
  slug: DnaSequenceRequestRegistryFields
- name: DnaSequenceSummary
  property_count: 3
  slug: DnaSequenceSummary
- name: DnaSequenceTranscription
  property_count: 4
  slug: DnaSequenceTranscription
- name: DnaSequenceUpdate
  property_count: 0
  slug: DnaSequenceUpdate
- name: DnaSequenceUpsertRequest
  property_count: 0
  slug: DnaSequenceUpsertRequest
- name: DnaSequenceWithEntityType
  property_count: 0
  slug: DnaSequenceWithEntityType
- name: DnaSequencesArchivalChange
  property_count: 2
  slug: DnaSequencesArchivalChange
- name: DnaSequencesArchive
  property_count: 2
  slug: DnaSequencesArchive
- name: DnaSequencesBulkCreateRequest
  property_count: 1
  slug: DnaSequencesBulkCreateRequest
- name: DnaSequencesBulkGet
  property_count: 1
  slug: DnaSequencesBulkGet
- name: DnaSequencesBulkUpdateRequest
  property_count: 1
  slug: DnaSequencesBulkUpdateRequest
- name: DnaSequencesBulkUpsertRequest
  property_count: 1
  slug: DnaSequencesBulkUpsertRequest
- name: DnaSequencesFindMatchingRegion
  property_count: 3
  slug: DnaSequencesFindMatchingRegion
- name: DnaSequencesPaginatedList
  property_count: 2
  slug: DnaSequencesPaginatedList
- name: DnaSequencesUnarchive
  property_count: 1
  slug: DnaSequencesUnarchive
- name: DnaTemplateAlignmentCreate
  property_count: 0
  slug: DnaTemplateAlignmentCreate
- name: DnaTemplateAlignmentFile
  property_count: 2
  slug: DnaTemplateAlignmentFile
- name: Dropdown
  property_count: 0
  slug: Dropdown
- name: DropdownCreate
  property_count: 3
  slug: DropdownCreate
- name: DropdownFieldDefinition
  property_count: 0
  slug: DropdownFieldDefinition
- name: DropdownMultiValueUiBlock
  property_count: 0
  slug: DropdownMultiValueUiBlock
- name: DropdownMultiValueUiBlockCreate
  property_count: 0
  slug: DropdownMultiValueUiBlockCreate
- name: DropdownMultiValueUiBlockUpdate
  property_count: 0
  slug: DropdownMultiValueUiBlockUpdate
- name: DropdownOption
  property_count: 3
  slug: DropdownOption
- name: DropdownOptionCreate
  property_count: 1
  slug: DropdownOptionCreate
- name: DropdownOptionUpdate
  property_count: 2
  slug: DropdownOptionUpdate
- name: DropdownOptionsArchivalChange
  property_count: 1
  slug: DropdownOptionsArchivalChange
- name: DropdownOptionsArchive
  property_count: 2
  slug: DropdownOptionsArchive
- name: DropdownOptionsUnarchive
  property_count: 1
  slug: DropdownOptionsUnarchive
- name: DropdownSummariesPaginatedList
  property_count: 2
  slug: DropdownSummariesPaginatedList
- name: DropdownSummary
  property_count: 2
  slug: DropdownSummary
- name: DropdownUiBlock
  property_count: 0
  slug: DropdownUiBlock
- name: DropdownUiBlockCreate
  property_count: 0
  slug: DropdownUiBlockCreate
- name: DropdownUiBlockUpdate
  property_count: 0
  slug: DropdownUiBlockUpdate
- name: DropdownUpdate
  property_count: 1
  slug: DropdownUpdate
- name: DropdownsRegistryList
  property_count: 1
  slug: DropdownsRegistryList
- name: EmptyObject
  property_count: 0
  slug: EmptyObject
- name: EntitiesBulkUpsertRequest
  property_count: 6
  slug: EntitiesBulkUpsertRequest
- name: Entity
  property_count: 0
  slug: Entity
- name: EntityArchiveReason
  property_count: 0
  slug: EntityArchiveReason
- name: EntityBulkUpsertBaseRequest
  property_count: 0
  slug: EntityBulkUpsertBaseRequest
- name: EntityLabels
  property_count: 3
  slug: EntityLabels
- name: EntityOrInaccessibleResource
  property_count: 0
  slug: EntityOrInaccessibleResource
- name: EntityRegisteredEvent
  property_count: 0
  slug: EntityRegisteredEvent
- name: EntitySchema
  property_count: 0
  slug: EntitySchema
- name: EntitySchemaAppConfigItem
  property_count: 0
  slug: EntitySchemaAppConfigItem
- name: EntitySchemasPaginatedList
  property_count: 2
  slug: EntitySchemasPaginatedList
- name: EntityUpsertBaseRequest
  property_count: 5
  slug: EntityUpsertBaseRequest
- name: Entries
  property_count: 1
  slug: Entries
- name: EntriesArchivalChange
  property_count: 1
  slug: EntriesArchivalChange
- name: EntriesArchive
  property_count: 2
  slug: EntriesArchive
- name: EntriesPaginatedList
  property_count: 2
  slug: EntriesPaginatedList
- name: EntriesUnarchive
  property_count: 1
  slug: EntriesUnarchive
- name: Entry
  property_count: 18
  slug: Entry
- name: EntryById
  property_count: 1
  slug: EntryById
- name: EntryCreate
  property_count: 8
  slug: EntryCreate
- name: EntryCreatedEvent
  property_count: 0
  slug: EntryCreatedEvent
- name: EntryDay
  property_count: 3
  slug: EntryDay
- name: EntryExternalFile
  property_count: 4
  slug: EntryExternalFile
- name: EntryExternalFileById
  property_count: 1
  slug: EntryExternalFileById
- name: EntryLink
  property_count: 3
  slug: EntryLink
- name: EntryNotePart
  property_count: 0
  slug: EntryNotePart
- name: EntryReviewProcess
  property_count: 5
  slug: EntryReviewProcess
- name: EntrySchema
  property_count: 3
  slug: EntrySchema
- name: EntrySchemaDetailed
  property_count: 0
  slug: EntrySchemaDetailed
- name: EntrySchemasPaginatedList
  property_count: 2
  slug: EntrySchemasPaginatedList
- name: EntryTable
  property_count: 3
  slug: EntryTable
- name: EntryTableCell
  property_count: 2
  slug: EntryTableCell
- name: EntryTableRow
  property_count: 1
  slug: EntryTableRow
- name: EntryTemplate
  property_count: 12
  slug: EntryTemplate
- name: EntryTemplateDay
  property_count: 3
  slug: EntryTemplateDay
- name: EntryTemplateUpdate
  property_count: 5
  slug: EntryTemplateUpdate
- name: EntryTemplatesPaginatedList
  property_count: 2
  slug: EntryTemplatesPaginatedList
- name: EntryUpdate
  property_count: 5
  slug: EntryUpdate
- name: EntryUpdatedAssignedReviewersEvent
  property_count: 0
  slug: EntryUpdatedAssignedReviewersEvent
- name: EntryUpdatedFieldsEvent
  property_count: 0
  slug: EntryUpdatedFieldsEvent
- name: EntryUpdatedReviewRecordEvent
  property_count: 0
  slug: EntryUpdatedReviewRecordEvent
- name: EntryUpdatedReviewSnapshotBetaEvent
  property_count: 0
  slug: EntryUpdatedReviewSnapshotBetaEvent
- name: Enzyme
  property_count: 6
  slug: Enzyme
- name: EnzymesPaginatedList
  property_count: 0
  slug: EnzymesPaginatedList
- name: Event
  property_count: 0
  slug: Event
- name: EventBase
  property_count: 5
  slug: EventBase
- name: EventsPaginatedList
  property_count: 2
  slug: EventsPaginatedList
- name: ExecuteSampleGroups
  property_count: 0
  slug: ExecuteSampleGroups
- name: ExperimentalWellRole
  property_count: 3
  slug: ExperimentalWellRole
- name: ExportAuditLogAsyncTask
  property_count: 0
  slug: ExportAuditLogAsyncTask
- name: ExportItemRequest
  property_count: 2
  slug: ExportItemRequest
- name: ExportsAsyncTask
  property_count: 0
  slug: ExportsAsyncTask
- name: ExternalFileNotePart
  property_count: 0
  slug: ExternalFileNotePart
- name: Feature
  property_count: 0
  slug: Feature
- name: FeatureBase
  property_count: 5
  slug: FeatureBase
- name: FeatureBulkCreate
  property_count: 0
  slug: FeatureBulkCreate
- name: FeatureCreate
  property_count: 0
  slug: FeatureCreate
- name: FeatureLibrariesPaginatedList
  property_count: 0
  slug: FeatureLibrariesPaginatedList
- name: FeatureLibrary
  property_count: 0
  slug: FeatureLibrary
- name: FeatureLibraryBase
  property_count: 2
  slug: FeatureLibraryBase
- name: FeatureLibraryCreate
  property_count: 0
  slug: FeatureLibraryCreate
- name: FeatureLibraryUpdate
  property_count: 0
  slug: FeatureLibraryUpdate
- name: FeatureUpdate
  property_count: 0
  slug: FeatureUpdate
- name: FeaturesBulkCreateRequest
  property_count: 1
  slug: FeaturesBulkCreateRequest
- name: FeaturesPaginatedList
  property_count: 0
  slug: FeaturesPaginatedList
- name: Field
  property_count: 5
  slug: Field
- name: FieldAppConfigItem
  property_count: 0
  slug: FieldAppConfigItem
- name: FieldDefinition
  property_count: 6
  slug: FieldDefinition
- name: FieldType
  property_count: 0
  slug: FieldType
- name: FieldValueWithResolution
  property_count: 0
  slug: FieldValueWithResolution
- name: FieldWithResolution
  property_count: 0
  slug: FieldWithResolution
- name: Fields
  property_count: 0
  slug: Fields
- name: FieldsWithResolution
  property_count: 0
  slug: FieldsWithResolution
- name: File
  property_count: 0
  slug: File
- name: FileCreate
  property_count: 4
  slug: FileCreate
- name: FileStatus
  property_count: 2
  slug: FileStatus
- name: FileUpdate
  property_count: 4
  slug: FileUpdate
- name: FileUploadUiBlock
  property_count: 0
  slug: FileUploadUiBlock
- name: FileUploadUiBlockCreate
  property_count: 0
  slug: FileUploadUiBlockCreate
- name: FileUploadUiBlockUpdate
  property_count: 0
  slug: FileUploadUiBlockUpdate
- name: FilesArchivalChange
  property_count: 1
  slug: FilesArchivalChange
- name: FilesArchive
  property_count: 2
  slug: FilesArchive
- name: FilesPaginatedList
  property_count: 2
  slug: FilesPaginatedList
- name: FilesUnarchive
  property_count: 1
  slug: FilesUnarchive
- name: FindMatchingRegionsAsyncTask
  property_count: 0
  slug: FindMatchingRegionsAsyncTask
- name: FindMatchingRegionsDnaAsyncTask
  property_count: 0
  slug: FindMatchingRegionsDnaAsyncTask
- name: FloatAppConfigItem
  property_count: 0
  slug: FloatAppConfigItem
- name: FloatFieldDefinition
  property_count: 0
  slug: FloatFieldDefinition
- name: Folder
  property_count: 5
  slug: Folder
- name: FolderCreate
  property_count: 2
  slug: FolderCreate
- name: FoldersArchivalChange
  property_count: 8
  slug: FoldersArchivalChange
- name: FoldersArchive
  property_count: 2
  slug: FoldersArchive
- name: FoldersPaginatedList
  property_count: 2
  slug: FoldersPaginatedList
- name: FoldersUnarchive
  property_count: 1
  slug: FoldersUnarchive
- name: ForbiddenError
  property_count: 1
  slug: ForbiddenError
- name: ForbiddenRestrictedSampleError
  property_count: 1
  slug: ForbiddenRestrictedSampleError
- name: GenericApiIdentifiedAppConfigItem
  property_count: 0
  slug: GenericApiIdentifiedAppConfigItem
- name: GenericEntity
  property_count: 17
  slug: GenericEntity
- name: InaccessibleResource
  property_count: 3
  slug: InaccessibleResource
- name: Ingredient
  property_count: 10
  slug: Ingredient
- name: IngredientMeasurementUnits
  property_count: 0
  slug: IngredientMeasurementUnits
- name: IngredientWriteParams
  property_count: 8
  slug: IngredientWriteParams
- name: InitialTable
  property_count: 2
  slug: InitialTable
- name: InstrumentQuery
  property_count: 8
  slug: InstrumentQuery
- name: IntegerAppConfigItem
  property_count: 0
  slug: IntegerAppConfigItem
- name: IntegerFieldDefinition
  property_count: 0
  slug: IntegerFieldDefinition
- name: InteractiveUiBlock
  property_count: 2
  slug: InteractiveUiBlock
- name: InventoryContainerTableNotePart
  property_count: 0
  slug: InventoryContainerTableNotePart
- name: InventoryPlateTableNotePart
  property_count: 0
  slug: InventoryPlateTableNotePart
- name: JsonAppConfigItem
  property_count: 0
  slug: JsonAppConfigItem
- name: LabAutomationBenchlingAppError
  property_count: 1
  slug: LabAutomationBenchlingAppError
- name: LabAutomationBenchlingAppErrors
  property_count: 1
  slug: LabAutomationBenchlingAppErrors
- name: LabAutomationTransform
  property_count: 9
  slug: LabAutomationTransform
- name: LabAutomationTransformUpdate
  property_count: 2
  slug: LabAutomationTransformUpdate
- name: LabelTemplate
  property_count: 3
  slug: LabelTemplate
- name: LabelTemplatesList
  property_count: 1
  slug: LabelTemplatesList
- name: LegacyWorkflow
  property_count: 6
  slug: LegacyWorkflow
- name: LegacyWorkflowList
  property_count: 1
  slug: LegacyWorkflowList
- name: LegacyWorkflowPatch
  property_count: 3
  slug: LegacyWorkflowPatch
- name: LegacyWorkflowSample
  property_count: 5
  slug: LegacyWorkflowSample
- name: LegacyWorkflowSampleList
  property_count: 1
  slug: LegacyWorkflowSampleList
- name: LegacyWorkflowStage
  property_count: 3
  slug: LegacyWorkflowStage
- name: LegacyWorkflowStageList
  property_count: 1
  slug: LegacyWorkflowStageList
- name: LegacyWorkflowStageRun
  property_count: 4
  slug: LegacyWorkflowStageRun
- name: LegacyWorkflowStageRunList
  property_count: 1
  slug: LegacyWorkflowStageRunList
- name: LinkedAppConfigResource
  property_count: 0
  slug: LinkedAppConfigResource
- name: LinkedAppConfigResourceMixin
  property_count: 1
  slug: LinkedAppConfigResourceMixin
- name: LinkedAppConfigResourceSummary
  property_count: 2
  slug: LinkedAppConfigResourceSummary
- name: ListingError
  property_count: 1
  slug: ListingError
- name: Location
  property_count: 14
  slug: Location
- name: LocationCreate
  property_count: 5
  slug: LocationCreate
- name: LocationSchema
  property_count: 0
  slug: LocationSchema
- name: LocationSchemasList
  property_count: 1
  slug: LocationSchemasList
- name: LocationSchemasPaginatedList
  property_count: 0
  slug: LocationSchemasPaginatedList
- name: LocationUpdate
  property_count: 3
  slug: LocationUpdate
- name: LocationsArchivalChange
  property_count: 4
  slug: LocationsArchivalChange
- name: LocationsArchive
  property_count: 3
  slug: LocationsArchive
- name: LocationsBulkGet
  property_count: 1
  slug: LocationsBulkGet
- name: LocationsPaginatedList
  property_count: 2
  slug: LocationsPaginatedList
- name: LocationsUnarchive
  property_count: 1
  slug: LocationsUnarchive
- name: LookupTableNotePart
  property_count: 0
  slug: LookupTableNotePart
- name: MafftOptions
  property_count: 6
  slug: MafftOptions
- name: MarkdownUiBlock
  property_count: 3
  slug: MarkdownUiBlock
- name: MarkdownUiBlockCreate
  property_count: 0
  slug: MarkdownUiBlockCreate
- name: MarkdownUiBlockUpdate
  property_count: 0
  slug: MarkdownUiBlockUpdate
- name: MatchBasesRequest
  property_count: 6
  slug: MatchBasesRequest
- name: Measurement
  property_count: 2
  slug: Measurement
- name: Membership
  property_count: 2
  slug: Membership
- name: MembershipCreate
  property_count: 2
  slug: MembershipCreate
- name: MembershipUpdate
  property_count: 1
  slug: MembershipUpdate
- name: MembershipsPaginatedList
  property_count: 0
  slug: MembershipsPaginatedList
- name: Mixture
  property_count: 21
  slug: Mixture
- name: MixtureBulkUpdate
  property_count: 0
  slug: MixtureBulkUpdate
- name: MixtureCreate
  property_count: 0
  slug: MixtureCreate
- name: MixtureMeasurementUnits
  property_count: 0
  slug: MixtureMeasurementUnits
- name: MixturePrepTableNotePart
  property_count: 0
  slug: MixturePrepTableNotePart
- name: MixtureUpdate
  property_count: 11
  slug: MixtureUpdate
- name: MixtureWithEntityType
  property_count: 0
  slug: MixtureWithEntityType
- name: MixturesArchivalChange
  property_count: 1
  slug: MixturesArchivalChange
- name: MixturesArchive
  property_count: 2
  slug: MixturesArchive
- name: MixturesBulkCreateRequest
  property_count: 1
  slug: MixturesBulkCreateRequest
- name: MixturesBulkUpdateRequest
  property_count: 1
  slug: MixturesBulkUpdateRequest
- name: MixturesPaginatedList
  property_count: 2
  slug: MixturesPaginatedList
- name: MixturesUnarchive
  property_count: 1
  slug: MixturesUnarchive
- name: Molecule
  property_count: 19
  slug: Molecule
- name: MoleculeBaseRequest
  property_count: 8
  slug: MoleculeBaseRequest
- name: MoleculeBaseRequestForCreate
  property_count: 0
  slug: MoleculeBaseRequestForCreate
- name: MoleculeBulkUpdate
  property_count: 0
  slug: MoleculeBulkUpdate
- name: MoleculeBulkUpsertRequest
  property_count: 0
  slug: MoleculeBulkUpsertRequest
- name: MoleculeCreate
  property_count: 0
  slug: MoleculeCreate
- name: MoleculeStructure
  property_count: 2
  slug: MoleculeStructure
- name: MoleculeUpdate
  property_count: 0
  slug: MoleculeUpdate
- name: MoleculeUpsertRequest
  property_count: 0
  slug: MoleculeUpsertRequest
- name: MoleculeWithEntityType
  property_count: 0
  slug: MoleculeWithEntityType
- name: MoleculesArchivalChange
  property_count: 2
  slug: MoleculesArchivalChange
- name: MoleculesArchive
  property_count: 2
  slug: MoleculesArchive
- name: MoleculesBulkCreateRequest
  property_count: 1
  slug: MoleculesBulkCreateRequest
- name: MoleculesBulkUpdateRequest
  property_count: 1
  slug: MoleculesBulkUpdateRequest
- name: MoleculesBulkUpsertRequest
  property_count: 1
  slug: MoleculesBulkUpsertRequest
- name: MoleculesPaginatedList
  property_count: 0
  slug: MoleculesPaginatedList
- name: MoleculesUnarchive
  property_count: 1
  slug: MoleculesUnarchive
- name: Monomer
  property_count: 17
  slug: Monomer
- name: MonomerBaseRequest
  property_count: 6
  slug: MonomerBaseRequest
- name: MonomerCreate
  property_count: 0
  slug: MonomerCreate
- name: MonomerPolymerType
  property_count: 0
  slug: MonomerPolymerType
- name: MonomerType
  property_count: 0
  slug: MonomerType
- name: MonomerUpdate
  property_count: 0
  slug: MonomerUpdate
- name: MonomerVisualSymbol
  property_count: 0
  slug: MonomerVisualSymbol
- name: MonomersArchivalChange
  property_count: 2
  slug: MonomersArchivalChange
- name: MonomersArchive
  property_count: 2
  slug: MonomersArchive
- name: MonomersPaginatedList
  property_count: 0
  slug: MonomersPaginatedList
- name: MonomersUnarchive
  property_count: 1
  slug: MonomersUnarchive
- name: MultipleContainersTransfer
  property_count: 0
  slug: MultipleContainersTransfer
- name: MultipleContainersTransfersList
  property_count: 1
  slug: MultipleContainersTransfersList
- name: NameTemplatePart
  property_count: 4
  slug: NameTemplatePart
- name: NamingStrategy
  property_count: 0
  slug: NamingStrategy
- name: NotFoundError
  property_count: 1
  slug: NotFoundError
- name: NucleotideAlignment
  property_count: 0
  slug: NucleotideAlignment
- name: NucleotideAlignmentBase
  property_count: 5
  slug: NucleotideAlignmentBase
- name: NucleotideAlignmentFile
  property_count: 2
  slug: NucleotideAlignmentFile
- name: NucleotideAlignmentSummary
  property_count: 7
  slug: NucleotideAlignmentSummary
- name: NucleotideAlignmentsPaginatedList
  property_count: 0
  slug: NucleotideAlignmentsPaginatedList
- name: NucleotideConsensusAlignmentCreate
  property_count: 0
  slug: NucleotideConsensusAlignmentCreate
- name: NucleotideSequencePart
  property_count: 3
  slug: NucleotideSequencePart
- name: NucleotideTemplateAlignmentCreate
  property_count: 0
  slug: NucleotideTemplateAlignmentCreate
- name: OAuthBadRequestError
  property_count: 1
  slug: OAuthBadRequestError
- name: OAuthUnauthorizedError
  property_count: 1
  slug: OAuthUnauthorizedError
- name: Oligo
  property_count: 20
  slug: Oligo
- name: OligoBaseRequest
  property_count: 8
  slug: OligoBaseRequest
- name: OligoBaseRequestForCreate
  property_count: 0
  slug: OligoBaseRequestForCreate
- name: OligoBulkUpsertRequest
  property_count: 0
  slug: OligoBulkUpsertRequest
- name: OligoCreate
  property_count: 0
  slug: OligoCreate
- name: OligoUpdate
  property_count: 0
  slug: OligoUpdate
- name: OligoUpsertRequest
  property_count: 0
  slug: OligoUpsertRequest
- name: OligosArchivalChange
  property_count: 2
  slug: OligosArchivalChange
- name: OligosArchive
  property_count: 2
  slug: OligosArchive
- name: OligosBulkCreateRequest
  property_count: 1
  slug: OligosBulkCreateRequest
- name: OligosBulkGet
  property_count: 1
  slug: OligosBulkGet
- name: OligosPaginatedList
  property_count: 0
  slug: OligosPaginatedList
- name: OligosUnarchive
  property_count: 1
  slug: OligosUnarchive
- name: OptimizeCodons
  property_count: 11
  slug: OptimizeCodons
- name: Organization
  property_count: 3
  slug: Organization
- name: OrganizationSummary
  property_count: 3
  slug: OrganizationSummary
- name: OrganizationsPaginatedList
  property_count: 0
  slug: OrganizationsPaginatedList
- name: Pagination
  property_count: 1
  slug: Pagination
- name: PartySummary
  property_count: 3
  slug: PartySummary
- name: Plate
  property_count: 17
  slug: Plate
- name: PlateCreate
  property_count: 8
  slug: PlateCreate
- name: PlateCreationTableNotePart
  property_count: 0
  slug: PlateCreationTableNotePart
- name: PlateSchema
  property_count: 0
  slug: PlateSchema
- name: PlateSchemasList
  property_count: 1
  slug: PlateSchemasList
- name: PlateSchemasPaginatedList
  property_count: 0
  slug: PlateSchemasPaginatedList
- name: PlateUpdate
  property_count: 4
  slug: PlateUpdate
- name: PlatesArchivalChange
  property_count: 2
  slug: PlatesArchivalChange
- name: PlatesArchive
  property_count: 3
  slug: PlatesArchive
- name: PlatesBulkGet
  property_count: 1
  slug: PlatesBulkGet
- name: PlatesPaginatedList
  property_count: 2
  slug: PlatesPaginatedList
- name: PlatesUnarchive
  property_count: 1
  slug: PlatesUnarchive
- name: Primer
  property_count: 9
  slug: Primer
- name: PrintLabels
  property_count: 3
  slug: PrintLabels
- name: Printer
  property_count: 6
  slug: Printer
- name: PrintersList
  property_count: 1
  slug: PrintersList
- name: Project
  property_count: 4
  slug: Project
- name: ProjectsArchivalChange
  property_count: 9
  slug: ProjectsArchivalChange
- name: ProjectsArchive
  property_count: 2
  slug: ProjectsArchive
- name: ProjectsPaginatedList
  property_count: 2
  slug: ProjectsPaginatedList
- name: ProjectsUnarchive
  property_count: 1
  slug: ProjectsUnarchive
- name: ReducedPattern
  property_count: 2
  slug: ReducedPattern
- name: RegisterEntities
  property_count: 2
  slug: RegisterEntities
- name: RegisteredEntitiesList
  property_count: 1
  slug: RegisteredEntitiesList
- name: RegistrationOrigin
  property_count: 2
  slug: RegistrationOrigin
- name: RegistrationTableNotePart
  property_count: 0
  slug: RegistrationTableNotePart
- name: RegistriesList
  property_count: 1
  slug: RegistriesList
- name: Registry
  property_count: 4
  slug: Registry
- name: RegistrySchema
  property_count: 0
  slug: RegistrySchema
- name: Request
  property_count: 0
  slug: Request
- name: RequestBase
  property_count: 0
  slug: RequestBase
- name: RequestCreate
  property_count: 0
  slug: RequestCreate
- name: RequestCreatedEvent
  property_count: 0
  slug: RequestCreatedEvent
- name: RequestFulfillment
  property_count: 7
  slug: RequestFulfillment
- name: RequestFulfillmentsPaginatedList
  property_count: 2
  slug: RequestFulfillmentsPaginatedList
- name: RequestResponse
  property_count: 2
  slug: RequestResponse
- name: RequestResponseSamplesItemBatch
  property_count: 0
  slug: RequestResponseSamplesItemBatch
- name: RequestResponseSamplesItemEntity
  property_count: 0
  slug: RequestResponseSamplesItemEntity
- name: RequestSampleGroup
  property_count: 2
  slug: RequestSampleGroup
- name: RequestSampleGroupCreate
  property_count: 1
  slug: RequestSampleGroupCreate
- name: RequestSampleGroupSamples
  property_count: 0
  slug: RequestSampleGroupSamples
- name: RequestSampleWithBatch
  property_count: 2
  slug: RequestSampleWithBatch
- name: RequestSampleWithEntity
  property_count: 2
  slug: RequestSampleWithEntity
- name: RequestSchema
  property_count: 0
  slug: RequestSchema
- name: RequestSchemasPaginatedList
  property_count: 2
  slug: RequestSchemasPaginatedList
- name: RequestStatus
  property_count: 0
  slug: RequestStatus
- name: RequestTask
  property_count: 1
  slug: RequestTask
- name: RequestTaskBase
  property_count: 1
  slug: RequestTaskBase
- name: RequestTaskBaseFields
  property_count: 2
  slug: RequestTaskBaseFields
- name: RequestTaskSchema
  property_count: 0
  slug: RequestTaskSchema
- name: RequestTaskSchemasPaginatedList
  property_count: 2
  slug: RequestTaskSchemasPaginatedList
- name: RequestTasksBulkCreate
  property_count: 1
  slug: RequestTasksBulkCreate
- name: RequestTasksBulkCreateRequest
  property_count: 1
  slug: RequestTasksBulkCreateRequest
- name: RequestTasksBulkCreateResponse
  property_count: 1
  slug: RequestTasksBulkCreateResponse
- name: RequestTasksBulkUpdateRequest
  property_count: 1
  slug: RequestTasksBulkUpdateRequest
- name: RequestTasksBulkUpdateResponse
  property_count: 1
  slug: RequestTasksBulkUpdateResponse
- name: RequestTeamAssignee
  property_count: 1
  slug: RequestTeamAssignee
- name: RequestUpdate
  property_count: 0
  slug: RequestUpdate
- name: RequestUpdatedFieldsEvent
  property_count: 0
  slug: RequestUpdatedFieldsEvent
- name: RequestUserAssignee
  property_count: 1
  slug: RequestUserAssignee
- name: RequestWriteBase
  property_count: 0
  slug: RequestWriteBase
- name: RequestWriteTeamAssignee
  property_count: 1
  slug: RequestWriteTeamAssignee
- name: RequestWriteUserAssignee
  property_count: 1
  slug: RequestWriteUserAssignee
- name: RequestsBulkGet
  property_count: 1
  slug: RequestsBulkGet
- name: RequestsPaginatedList
  property_count: 0
  slug: RequestsPaginatedList
- name: ResultsTableNotePart
  property_count: 0
  slug: ResultsTableNotePart
- name: ReviewChange
  property_count: 6
  slug: ReviewChange
- name: ReviewSnapshot
  property_count: 5
  slug: ReviewSnapshot
- name: RnaAnnotation
  property_count: 0
  slug: RnaAnnotation
- name: RnaOligo
  property_count: 0
  slug: RnaOligo
- name: RnaOligoBulkUpdate
  property_count: 0
  slug: RnaOligoBulkUpdate
- name: RnaOligoCreate
  property_count: 0
  slug: RnaOligoCreate
- name: RnaOligoUpdate
  property_count: 0
  slug: RnaOligoUpdate
- name: RnaOligoWithEntityType
  property_count: 0
  slug: RnaOligoWithEntityType
- name: RnaOligosArchivalChange
  property_count: 2
  slug: RnaOligosArchivalChange
- name: RnaOligosArchive
  property_count: 2
  slug: RnaOligosArchive
- name: RnaOligosBulkCreateRequest
  property_count: 1
  slug: RnaOligosBulkCreateRequest
- name: RnaOligosBulkUpdateRequest
  property_count: 1
  slug: RnaOligosBulkUpdateRequest
- name: RnaOligosBulkUpsertRequest
  property_count: 1
  slug: RnaOligosBulkUpsertRequest
- name: RnaOligosPaginatedList
  property_count: 0
  slug: RnaOligosPaginatedList
- name: RnaOligosUnarchive
  property_count: 1
  slug: RnaOligosUnarchive
- name: RnaSequence
  property_count: 29
  slug: RnaSequence
- name: RnaSequenceBaseRequest
  property_count: 0
  slug: RnaSequenceBaseRequest
- name: RnaSequenceBaseRequestForCreate
  property_count: 0
  slug: RnaSequenceBaseRequestForCreate
- name: RnaSequenceBulkCreate
  property_count: 0
  slug: RnaSequenceBulkCreate
- name: RnaSequenceBulkUpdate
  property_count: 0
  slug: RnaSequenceBulkUpdate
- name: RnaSequenceCreate
  property_count: 0
  slug: RnaSequenceCreate
- name: RnaSequencePart
  property_count: 0
  slug: RnaSequencePart
- name: RnaSequenceRequestRegistryFields
  property_count: 1
  slug: RnaSequenceRequestRegistryFields
- name: RnaSequenceUpdate
  property_count: 0
  slug: RnaSequenceUpdate
- name: RnaSequenceWithEntityType
  property_count: 0
  slug: RnaSequenceWithEntityType
- name: RnaSequencesArchivalChange
  property_count: 1
  slug: RnaSequencesArchivalChange
- name: RnaSequencesArchive
  property_count: 2
  slug: RnaSequencesArchive
- name: RnaSequencesBulkCreateRequest
  property_count: 1
  slug: RnaSequencesBulkCreateRequest
- name: RnaSequencesBulkGet
  property_count: 1
  slug: RnaSequencesBulkGet
- name: RnaSequencesBulkUpdateRequest
  property_count: 1
  slug: RnaSequencesBulkUpdateRequest
- name: RnaSequencesPaginatedList
  property_count: 2
  slug: RnaSequencesPaginatedList
- name: RnaSequencesUnarchive
  property_count: 1
  slug: RnaSequencesUnarchive
- name: SampleGroup
  property_count: 2
  slug: SampleGroup
- name: SampleGroupStatus
  property_count: 0
  slug: SampleGroupStatus
- name: SampleGroupStatusUpdate
  property_count: 2
  slug: SampleGroupStatusUpdate
- name: SampleGroupsStatusUpdate
  property_count: 1
  slug: SampleGroupsStatusUpdate
- name: SampleRestrictionStatus
  property_count: 0
  slug: SampleRestrictionStatus
- name: Schema
  property_count: 5
  slug: Schema
- name: SchemaDependencySubtypes
  property_count: 0
  slug: SchemaDependencySubtypes
- name: SchemaFieldsQueryParam
  property_count: 0
  slug: SchemaFieldsQueryParam
- name: SchemaLinkFieldDefinition
  property_count: 0
  slug: SchemaLinkFieldDefinition
- name: SchemaSummary
  property_count: 2
  slug: SchemaSummary
- name: SearchBasesRequest
  property_count: 7
  slug: SearchBasesRequest
- name: SearchInputMultiValueUiBlock
  property_count: 0
  slug: SearchInputMultiValueUiBlock
- name: SearchInputMultiValueUiBlockCreate
  property_count: 0
  slug: SearchInputMultiValueUiBlockCreate
- name: SearchInputMultiValueUiBlockUpdate
  property_count: 0
  slug: SearchInputMultiValueUiBlockUpdate
- name: SearchInputUiBlock
  property_count: 0
  slug: SearchInputUiBlock
- name: SearchInputUiBlockCreate
  property_count: 0
  slug: SearchInputUiBlockCreate
- name: SearchInputUiBlockItemType
  property_count: 0
  slug: SearchInputUiBlockItemType
- name: SearchInputUiBlockUpdate
  property_count: 0
  slug: SearchInputUiBlockUpdate
- name: SectionUiBlock
  property_count: 0
  slug: SectionUiBlock
- name: SectionUiBlockCreate
  property_count: 0
  slug: SectionUiBlockCreate
- name: SectionUiBlockUpdate
  property_count: 0
  slug: SectionUiBlockUpdate
- name: SecureTextAppConfigItem
  property_count: 0
  slug: SecureTextAppConfigItem
- name: SelectorInputMultiValueUiBlock
  property_count: 0
  slug: SelectorInputMultiValueUiBlock
- name: SelectorInputMultiValueUiBlockCreate
  property_count: 0
  slug: SelectorInputMultiValueUiBlockCreate
- name: SelectorInputMultiValueUiBlockUpdate
  property_count: 0
  slug: SelectorInputMultiValueUiBlockUpdate
- name: SelectorInputUiBlock
  property_count: 0
  slug: SelectorInputUiBlock
- name: SelectorInputUiBlockCreate
  property_count: 0
  slug: SelectorInputUiBlockCreate
- name: SelectorInputUiBlockUpdate
  property_count: 0
  slug: SelectorInputUiBlockUpdate
- name: SequenceFeatureBase
  property_count: 4
  slug: SequenceFeatureBase
- name: SequenceFeatureCustomField
  property_count: 2
  slug: SequenceFeatureCustomField
- name: SimpleFieldDefinition
  property_count: 0
  slug: SimpleFieldDefinition
- name: SimpleNotePart
  property_count: 0
  slug: SimpleNotePart
- name: StageEntry
  property_count: 16
  slug: StageEntry
- name: StageEntryCreatedEvent
  property_count: 0
  slug: StageEntryCreatedEvent
- name: StageEntryUpdatedAssignedReviewersEvent
  property_count: 0
  slug: StageEntryUpdatedAssignedReviewersEvent
- name: StageEntryUpdatedFieldsEvent
  property_count: 0
  slug: StageEntryUpdatedFieldsEvent
- name: StageEntryUpdatedReviewRecordEvent
  property_count: 0
  slug: StageEntryUpdatedReviewRecordEvent
- name: StructuredTableApiIdentifiers
  property_count: 3
  slug: StructuredTableApiIdentifiers
- name: StructuredTableColumnInfo
  property_count: 3
  slug: StructuredTableColumnInfo
- name: TableNotePart
  property_count: 0
  slug: TableNotePart
- name: TableUiBlock
  property_count: 0
  slug: TableUiBlock
- name: TableUiBlockCreate
  property_count: 0
  slug: TableUiBlockCreate
- name: TableUiBlockDataFrameSource
  property_count: 2
  slug: TableUiBlockDataFrameSource
- name: TableUiBlockDatasetSource
  property_count: 2
  slug: TableUiBlockDatasetSource
- name: TableUiBlockSource
  property_count: 0
  slug: TableUiBlockSource
- name: TableUiBlockUpdate
  property_count: 0
  slug: TableUiBlockUpdate
- name: Team
  property_count: 0
  slug: Team
- name: TeamCreate
  property_count: 3
  slug: TeamCreate
- name: TeamSummary
  property_count: 0
  slug: TeamSummary
- name: TeamUpdate
  property_count: 2
  slug: TeamUpdate
- name: TeamsPaginatedList
  property_count: 0
  slug: TeamsPaginatedList
- name: TextAppConfigItem
  property_count: 0
  slug: TextAppConfigItem
- name: TextBoxNotePart
  property_count: 0
  slug: TextBoxNotePart
- name: TextInputUiBlock
  property_count: 0
  slug: TextInputUiBlock
- name: TextInputUiBlockCreate
  property_count: 0
  slug: TextInputUiBlockCreate
- name: TextInputUiBlockUpdate
  property_count: 0
  slug: TextInputUiBlockUpdate
- name: TokenCreate
  property_count: 3
  slug: TokenCreate
- name: TokenResponse
  property_count: 3
  slug: TokenResponse
- name: TransfersAsyncTask
  property_count: 0
  slug: TransfersAsyncTask
- name: Translation
  property_count: 0
  slug: Translation
- name: UnitSummary
  property_count: 4
  slug: UnitSummary
- name: UnregisterEntities
  property_count: 2
  slug: UnregisterEntities
- name: UpdateEventMixin
  property_count: 1
  slug: UpdateEventMixin
- name: User
  property_count: 0
  slug: User
- name: UserActivity
  property_count: 2
  slug: UserActivity
- name: UserBulkCreateRequest
  property_count: 1
  slug: UserBulkCreateRequest
- name: UserBulkUpdate
  property_count: 0
  slug: UserBulkUpdate
- name: UserBulkUpdateRequest
  property_count: 1
  slug: UserBulkUpdateRequest
- name: UserCreate
  property_count: 3
  slug: UserCreate
- name: UserInputMultiValueUiBlock
  property_count: 0
  slug: UserInputMultiValueUiBlock
- name: UserInputUiBlock
  property_count: 0
  slug: UserInputUiBlock
- name: UserSummary
  property_count: 0
  slug: UserSummary
- name: UserUpdate
  property_count: 4
  slug: UserUpdate
- name: UserValidation
  property_count: 2
  slug: UserValidation
- name: UsersPaginatedList
  property_count: 0
  slug: UsersPaginatedList
- name: WarehouseCredentialSummary
  property_count: 6
  slug: WarehouseCredentialSummary
- name: WarehouseCredentials
  property_count: 3
  slug: WarehouseCredentials
- name: WarehouseCredentialsCreate
  property_count: 1
  slug: WarehouseCredentialsCreate
- name: Well
  property_count: 22
  slug: Well
- name: WellOrInaccessibleResource
  property_count: 0
  slug: WellOrInaccessibleResource
- name: WorkflowEndNodeDetails
  property_count: 3
  slug: WorkflowEndNodeDetails
- name: WorkflowFlowchart
  property_count: 7
  slug: WorkflowFlowchart
- name: WorkflowFlowchartConfigSummary
  property_count: 2
  slug: WorkflowFlowchartConfigSummary
- name: WorkflowFlowchartConfigVersion
  property_count: 4
  slug: WorkflowFlowchartConfigVersion
- name: WorkflowFlowchartEdgeConfig
  property_count: 3
  slug: WorkflowFlowchartEdgeConfig
- name: WorkflowFlowchartNodeConfig
  property_count: 3
  slug: WorkflowFlowchartNodeConfig
- name: WorkflowFlowchartPaginatedList
  property_count: 2
  slug: WorkflowFlowchartPaginatedList
- name: WorkflowList
  property_count: 1
  slug: WorkflowList
- name: WorkflowNodeTaskGroupSummary
  property_count: 0
  slug: WorkflowNodeTaskGroupSummary
- name: WorkflowOutput
  property_count: 0
  slug: WorkflowOutput
- name: WorkflowOutputArchiveReason
  property_count: 0
  slug: WorkflowOutputArchiveReason
- name: WorkflowOutputBulkCreate
  property_count: 0
  slug: WorkflowOutputBulkCreate
- name: WorkflowOutputBulkUpdate
  property_count: 0
  slug: WorkflowOutputBulkUpdate
- name: WorkflowOutputCreate
  property_count: 0
  slug: WorkflowOutputCreate
- name: WorkflowOutputCreatedEvent
  property_count: 0
  slug: WorkflowOutputCreatedEvent
- name: WorkflowOutputNodeDetails
  property_count: 3
  slug: WorkflowOutputNodeDetails
- name: WorkflowOutputSchema
  property_count: 0
  slug: WorkflowOutputSchema
- name: WorkflowOutputSummary
  property_count: 2
  slug: WorkflowOutputSummary
- name: WorkflowOutputUpdate
  property_count: 0
  slug: WorkflowOutputUpdate
- name: WorkflowOutputUpdatedFieldsEvent
  property_count: 0
  slug: WorkflowOutputUpdatedFieldsEvent
- name: WorkflowOutputWriteBase
  property_count: 1
  slug: WorkflowOutputWriteBase
- name: WorkflowOutputsArchivalChange
  property_count: 1
  slug: WorkflowOutputsArchivalChange
- name: WorkflowOutputsArchive
  property_count: 2
  slug: WorkflowOutputsArchive
- name: WorkflowOutputsBulkCreateRequest
  property_count: 1
  slug: WorkflowOutputsBulkCreateRequest
- name: WorkflowOutputsBulkUpdateRequest
  property_count: 1
  slug: WorkflowOutputsBulkUpdateRequest
- name: WorkflowOutputsPaginatedList
  property_count: 2
  slug: WorkflowOutputsPaginatedList
- name: WorkflowOutputsUnarchive
  property_count: 1
  slug: WorkflowOutputsUnarchive
- name: WorkflowPatch
  property_count: 3
  slug: WorkflowPatch
- name: WorkflowRootNodeDetails
  property_count: 3
  slug: WorkflowRootNodeDetails
- name: WorkflowRouterFunction
  property_count: 4
  slug: WorkflowRouterFunction
- name: WorkflowRouterNodeDetails
  property_count: 4
  slug: WorkflowRouterNodeDetails
- name: WorkflowSample
  property_count: 5
  slug: WorkflowSample
- name: WorkflowSampleList
  property_count: 1
  slug: WorkflowSampleList
- name: WorkflowStage
  property_count: 3
  slug: WorkflowStage
- name: WorkflowStageList
  property_count: 1
  slug: WorkflowStageList
- name: WorkflowStageRun
  property_count: 4
  slug: WorkflowStageRun
- name: WorkflowStageRunList
  property_count: 1
  slug: WorkflowStageRunList
- name: WorkflowTask
  property_count: 0
  slug: WorkflowTask
- name: WorkflowTaskArchiveReason
  property_count: 0
  slug: WorkflowTaskArchiveReason
- name: WorkflowTaskBase
  property_count: 0
  slug: WorkflowTaskBase
- name: WorkflowTaskBulkCreate
  property_count: 0
  slug: WorkflowTaskBulkCreate
- name: WorkflowTaskBulkUpdate
  property_count: 0
  slug: WorkflowTaskBulkUpdate
- name: WorkflowTaskCreate
  property_count: 0
  slug: WorkflowTaskCreate
- name: WorkflowTaskCreatedEvent
  property_count: 0
  slug: WorkflowTaskCreatedEvent
- name: WorkflowTaskExecutionOrigin
  property_count: 3
  slug: WorkflowTaskExecutionOrigin
- name: WorkflowTaskGroup
  property_count: 0
  slug: WorkflowTaskGroup
- name: WorkflowTaskGroupArchiveReason
  property_count: 0
  slug: WorkflowTaskGroupArchiveReason
- name: WorkflowTaskGroupBase
  property_count: 0
  slug: WorkflowTaskGroupBase
- name: WorkflowTaskGroupCreate
  property_count: 0
  slug: WorkflowTaskGroupCreate
- name: WorkflowTaskGroupCreatedEvent
  property_count: 0
  slug: WorkflowTaskGroupCreatedEvent
- name: WorkflowTaskGroupMappingCompletedEvent
  property_count: 0
  slug: WorkflowTaskGroupMappingCompletedEvent
- name: WorkflowTaskGroupSummary
  property_count: 3
  slug: WorkflowTaskGroupSummary
- name: WorkflowTaskGroupUpdate
  property_count: 0
  slug: WorkflowTaskGroupUpdate
- name: WorkflowTaskGroupUpdatedWatchersEvent
  property_count: 0
  slug: WorkflowTaskGroupUpdatedWatchersEvent
- name: WorkflowTaskGroupWriteBase
  property_count: 3
  slug: WorkflowTaskGroupWriteBase
- name: WorkflowTaskGroupsArchivalChange
  property_count: 1
  slug: WorkflowTaskGroupsArchivalChange
- name: WorkflowTaskGroupsArchive
  property_count: 2
  slug: WorkflowTaskGroupsArchive
- name: WorkflowTaskGroupsPaginatedList
  property_count: 2
  slug: WorkflowTaskGroupsPaginatedList
- name: WorkflowTaskGroupsUnarchive
  property_count: 1
  slug: WorkflowTaskGroupsUnarchive
- name: WorkflowTaskNodeDetails
  property_count: 3
  slug: WorkflowTaskNodeDetails
- name: WorkflowTaskSchema
  property_count: 0
  slug: WorkflowTaskSchema
- name: WorkflowTaskSchemaBase
  property_count: 0
  slug: WorkflowTaskSchemaBase
- name: WorkflowTaskSchemaSummary
  property_count: 2
  slug: WorkflowTaskSchemaSummary
- name: WorkflowTaskSchemasPaginatedList
  property_count: 2
  slug: WorkflowTaskSchemasPaginatedList
- name: WorkflowTaskStatus
  property_count: 3
  slug: WorkflowTaskStatus
- name: WorkflowTaskStatusLifecycle
  property_count: 5
  slug: WorkflowTaskStatusLifecycle
- name: WorkflowTaskStatusLifecycleTransition
  property_count: 2
  slug: WorkflowTaskStatusLifecycleTransition
- name: WorkflowTaskSummary
  property_count: 2
  slug: WorkflowTaskSummary
- name: WorkflowTaskUpdate
  property_count: 0
  slug: WorkflowTaskUpdate
- name: WorkflowTaskUpdatedAssigneeEvent
  property_count: 0
  slug: WorkflowTaskUpdatedAssigneeEvent
- name: WorkflowTaskUpdatedFieldsEvent
  property_count: 0
  slug: WorkflowTaskUpdatedFieldsEvent
- name: WorkflowTaskUpdatedScheduledOnEvent
  property_count: 0
  slug: WorkflowTaskUpdatedScheduledOnEvent
- name: WorkflowTaskUpdatedStatusEvent
  property_count: 0
  slug: WorkflowTaskUpdatedStatusEvent
- name: WorkflowTaskWriteBase
  property_count: 3
  slug: WorkflowTaskWriteBase
- name: WorkflowTasksArchivalChange
  property_count: 1
  slug: WorkflowTasksArchivalChange
- name: WorkflowTasksArchive
  property_count: 2
  slug: WorkflowTasksArchive
- name: WorkflowTasksBulkCopyRequest
  property_count: 1
  slug: WorkflowTasksBulkCopyRequest
- name: WorkflowTasksBulkCreateRequest
  property_count: 1
  slug: WorkflowTasksBulkCreateRequest
- name: WorkflowTasksBulkUpdateRequest
  property_count: 1
  slug: WorkflowTasksBulkUpdateRequest
- name: WorkflowTasksPaginatedList
  property_count: 2
  slug: WorkflowTasksPaginatedList
- name: WorkflowTasksUnarchive
  property_count: 1
  slug: WorkflowTasksUnarchive
- name: WorksheetReviewChanges
  property_count: 9
  slug: WorksheetReviewChanges
- name: WorksheetUpdatedReviewSnapshotBetaEvent
  property_count: 0
  slug: WorksheetUpdatedReviewSnapshotBetaEvent
layout: provider
mcp_servers:
- description: 'Benchling operates an official, first-party REMOTE MCP server. It is wildcard-tenanted: every Benchling tenant gets its own host under *.mcp.benchling.com, and an MCP client POSTs to https://{tenant}.'
  name: Benchling MCP Server
  slug: benchling-mcp-server
modified: '2026-08-15'
name: Benchling
nav: Providers
network: true
overview: 'Benchling publishes 203 APIs on the [APIs.io](https://apis.io/) network, including AA Sequences API, Apps API, Assay Results API, and 200 more. Tagged areas include Life Sciences, Biotech, R&D, Molecular Biology, and Laboratory Information Management.


  The Benchling catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Benchling''s developer surface includes changelog, API reference, getting-started guide, support, pricing, signup flow, authentication, and 43 more developer resources.'
plans:
- name: Benchling Plans Pricing
  plan_count: 3
  slug: benchling-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Benchling Rate Limits
  slug: benchling-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Benchling API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: benchling-jsonschema-spectral-rules
scopes:
- name: Benchling Scopes
  scope_count: 0
  slug: benchling-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.1
  coverage:
    artifact_dirs: 31
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 28.0
    contract_quality: 61.4
    developer_ergonomics: 49.4
    discoverability: 70.4
    governance: 28.0
    operational_transparency: 69.7
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 203
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/benchling/refs/heads/main/screenshots/benchling-2026-06-20T173135.png
security:
- kind: authentication
  name: Benchling Authentication
  slug: benchling-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Benchling Domain Security
  slug: benchling-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Benchling Trust Center
  slug: benchling-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2025
slug: benchling
tags:
- Life Sciences
- Biotech
- R&D
- Molecular Biology
- Laboratory Information Management
- Electronic Lab Notebook
- Assay Management
- Inventory Management
- Sequence Management
- Experiment Workflows
- REST
- Webhook
website: https://www.benchling.com/developer-platform
---
