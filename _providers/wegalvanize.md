---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: An action is a specific follow-up measure that is associated with an identified issue. You can add actions and assign action owners. You can also set up reminders for yourself to retest issues or trac
  name: Wegalvanize Actions API
  slug: wegalvanize-actions-api
- description: The Activities API from Wegalvanize — 2 operation(s) for activities.
  name: Wegalvanize Activities API
  slug: wegalvanize-activities-api
- description: An analysis is a second-level container. Analyses live in collections, and they are used to organize tables. Once you have created a collection, you can add one or more analyses to that collection. Yo
  name: Wegalvanize Analyses API
  slug: wegalvanize-analyses-api
- description: Attachments are supporting files linked to Controls and Control Tests.
  name: Wegalvanize Attachments API
  slug: wegalvanize-attachments-api
- description: 'A collaborator is a representation of user roles, which are associated with projects and frameworks, that you can manipulate. Collaborators are accessible both in project and framework resources. The '
  name: Wegalvanize Collaborators API
  slug: wegalvanize-collaborators-api
- description: A collection is a container used to organize analyses that relate to different departments, business processes, or data sets. Collections are the highest level of organization in the Results app. Your
  name: Wegalvanize Collections API
  slug: wegalvanize-collections-api
- description: You can use Compliance Maps to associate industry standards and regulations with your control frameworks. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=pm-compliance-map
  name: Wegalvanize Compliance Maps API
  slug: wegalvanize-compliance-maps-api
- description: A control performance schedule is a schedule of control tests that are performed on a recurring basis. Control performance schedules are associated with controls. > **Note:** Control performance sched
  name: Wegalvanize Control performance schedules API
  slug: wegalvanize-control-performance-schedules-api
- description: A test plan is a document that details how controls are assessed. Test plans identify the testing method or type of evidence obtained, specify the total sample size (split amongst testing rounds), and
  name: Wegalvanize Control test plans API
  slug: wegalvanize-control-test-plans-api
- description: Control tests evaluate the operating effectiveness of a control. * If your project includes one testing round, each control you create has one corresponding control test. * If your project includes mu
  name: Wegalvanize Control tests API
  slug: wegalvanize-control-tests-api
- description: A control is a program, policy, routine, or activity that is intended to mitigate a risk. Controls are organized by objectives, and can be associated with one or more risks. The combination of identif
  name: Wegalvanize Controls API
  slug: wegalvanize-controls-api
- description: 'Custom attributes are the customizable fields that are associated with supported objects. Custom attributes are defined on the project type and used by the project and its children (i.e. objectives). '
  name: Wegalvanize Custom attributes API
  slug: wegalvanize-custom-attributes-api
- description: 'Entities may be business units, departments, locations, or key initiatives that are within the scope of the organization. Entities have a hierarchical structure composed of parent and child entities. '
  name: Wegalvanize Entities API
  slug: wegalvanize-entities-api
- description: A event report table stores responses to a questionnaire that are distributed through an anonymous link. Each event report table can hold a maximum of 100,000 rows, 500 columns, and 256 characters per
  name: Wegalvanize Event Reports API
  slug: wegalvanize-event-reports-api
- description: An Event links a status to handlers. When an event is fired, the associated handlers will be triggered.
  name: Wegalvanize Events API
  slug: wegalvanize-events-api
- description: Service to extract the resources from an organization based on resource ids.
  name: Wegalvanize Extract API
  slug: wegalvanize-extract-api
- description: The Flow Key API from Wegalvanize — 1 operation(s) for flow key.
  name: Wegalvanize Flow Key API
  slug: wegalvanize-flow-key-api
- description: A framework is a management system that allows you to define objectives, risks, and controls, perform tests, and compile information for reporting purposes. Frameworks may also be known as audits, com
  name: Wegalvanize Frameworks API
  slug: wegalvanize-frameworks-api
- description: Groups are a security feature in Launchpad that allow you to assign the same level of access to multiple users simultaneously. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cs
  name: Wegalvanize Groups API
  slug: wegalvanize-groups-api
- description: Handlers contain a set of conditions and actions that occur upon certain situation, e.g. an event fired, on scheduled time, a message received, etc.
  name: Wegalvanize Handlers API
  slug: wegalvanize-handlers-api
- description: Importer for HighBond, responsible for importing HighBond resources. You can bulk import HighBond resources if you want to avoid time-consuming manual data entry associated with individually adding re
  name: Wegalvanize Importer API
  slug: wegalvanize-importer-api
- description: An interpretation is a bundled collection of filters, visualizations, and statistics based on a table in a collection. Use them to interpret and visualize results to gain a deeper understanding of the
  name: Wegalvanize Interpretations API
  slug: wegalvanize-interpretations-api
- description: An issue is a problem, control gap, or exception that has been identified within a project. Adding an issue involves recording basic information about the issue and assigning the issue to an owner. Is
  name: Wegalvanize Issues API
  slug: wegalvanize-issues-api
- description: A metric is a calculation that you label as a specific type of key indicator. Key indicators are quantitative measurements of success (KPI, KCI) or risk (KRI) that are associated with a company's obje
  name: Wegalvanize Metrics API
  slug: wegalvanize-metrics-api
- description: '> **Note —** Only controls in projects that have an `"active"` state can be accessed using the API.'
  name: Wegalvanize Mitigations API
  slug: wegalvanize-mitigations-api
- description: 'A narrative is a description of a business process or area under review. Narratives are also known as policies, IT policies, process narratives, process descriptions, or control guides. > **Note:** > '
  name: Wegalvanize Narratives API
  slug: wegalvanize-narratives-api
- description: Use non-project time categories to divide non-project time entries by categories. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=pm-managing-timesheets" target="_blank">L
  name: Wegalvanize Non-project time categories API
  slug: wegalvanize-non-project-time-categories-api
- description: 'Objectives are the basis of a project or framework. They are also the organizing containers for the work done in a project or framework. Each objective states the subject matter under examination and '
  name: Wegalvanize Objectives API
  slug: wegalvanize-objectives-api
- description: A planning file (also known as a reference file) is a supporting document that relates to a project or framework. Planning files typically contain information associated with the planning phase of a p
  name: Wegalvanize Planning files API
  slug: wegalvanize-planning-files-api
- description: Project types define the structure of a project or framework, including the terminology used in the project or framework. Updates to project types apply to all active projects, archived projects, temp
  name: Wegalvanize Project types API
  slug: wegalvanize-project-types-api
- description: A project is a management system that allows you to define objectives, risks, and controls, perform tests, and compile information for reporting purposes. Projects may also be known as audits, complia
  name: Wegalvanize Projects API
  slug: wegalvanize-projects-api
- description: Questionnaires are used to gather information from respondents and contextualize data. Each Collection can have one or more questionnaires that you deploy as surveys, event reports, or as follow-up me
  name: Wegalvanize Questionnaires API
  slug: wegalvanize-questionnaires-api
- description: The Record columns API from Wegalvanize — 1 operation(s) for record columns.
  name: Wegalvanize Record columns API
  slug: wegalvanize-record-columns-api
- description: A dictionary of table record statuses
  name: Wegalvanize Record statuses API
  slug: wegalvanize-record-statuses-api
- description: Records are rows in a table. Each record can have multiple attributes with values.
  name: Wegalvanize Records API
  slug: wegalvanize-records-api
- description: Request statuses provide visibility into the progress of request resolutions. The number of available statuses, and the terms used for each status, can be customized by the organization. <a href="http
  name: Wegalvanize Request item statuses API
  slug: wegalvanize-request-item-statuses-api
- description: A request item is used by Auditors to request documentation from business owners and other stakeholders to gather further information. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Defaul
  name: Wegalvanize Request Items API
  slug: wegalvanize-request-items-api
- description: A results file is a supporting document or concluding memo that relates to a project. Results files typically contain information associated with the reporting phase of a project. > **Note —** Only re
  name: Wegalvanize Results files API
  slug: wegalvanize-results-files-api
- description: Results triggers are automation definitions created by users in the Results app.
  name: Wegalvanize Results Triggers API
  slug: wegalvanize-results-triggers-api
- description: Results users are users who have access to the Results app.
  name: Wegalvanize Results Users API
  slug: wegalvanize-results-users-api
- description: 'A risk is an effect of uncertainty on an objective, with the effect having a positive or negative deviation from what is expected. Risks are organized by objectives, and can be associated with one or '
  name: Wegalvanize Risks API
  slug: wegalvanize-risks-api
- description: 'The Robots app provides two environments for managing and running analytic scripts that you author in Analytics: **development mode** and **production**. In development mode, you can test newly commit'
  name: Wegalvanize Robot Activations API
  slug: wegalvanize-robot-activations-api
- description: An analytic script is a regular script with an analytic header. You can upload analytic scripts to a robot. The analytic header is a series of declarative tags that allow the script to run in the Robo
  name: Wegalvanize Robot Apps API
  slug: wegalvanize-robot-apps-api
- description: Robot collaborators are users who have access to that particular robot.
  name: Wegalvanize Robot Collaborators API
  slug: wegalvanize-robot-collaborators-api
- description: Related files in an ACL robot are non-Analytics files such as Excel or delimited that can be used as input for scripts in the robot. <a href="https://help.highbond.com/helpdocs/robotics/en-us/Default.
  name: Wegalvanize Robot Files API
  slug: wegalvanize-robot-files-api
- description: Robot task runs, also known as robot jobs, are individual executions of a robot task. For example, for any given robot task, you can schedule a task run once every 24 hours, or you can initiate a task
  name: Wegalvanize Robot Jobs API
  slug: wegalvanize-robot-jobs-api
- description: A version of a robot that includes the hcl script in json. You can upload new version of your hcl script to your highbond robot or workflow robot. Flow json includes python script, variables and syste
  name: Wegalvanize Robot Script Versions API
  slug: wegalvanize-robot-script-versions-api
- description: When you create a task, a robot runs the task according to the settings that you configure. A task can be scheduled or run ad hoc (manually). Each task has its own unique settings. <a href="https://he
  name: Wegalvanize Robot Tasks API
  slug: wegalvanize-robot-tasks-api
- description: Users of the Robots module including some Robots-specific fields. Only Robots Admins can access this endpoint.
  name: Wegalvanize Robot Users API
  slug: wegalvanize-robot-users-api
- description: Working files in a HighBond robot or a Workflow robot are files such as Excel or CSV that can be used as input for scripts in the robot.
  name: Wegalvanize Robot Working Files API
  slug: wegalvanize-robot-working-files-api
- description: A Robots Agent is the on-premise or cloud-based Robots component that uses the Analytics script engine to run scripts against data. <a href="https://help.highbond.com/helpdocs/robotics/en-us/Default.h
  name: Wegalvanize Robots Agents API
  slug: wegalvanize-robots-agents-api
- description: 'A robot is a tool that lets you automate repetitive tasks using scripts built in Analytics. Once you create the scripts, you upload them to a robot in the Robots app and configure the task automation '
  name: Wegalvanize Robots API
  slug: wegalvanize-robots-api
- description: Folders to organize Robots.
  name: Wegalvanize Robots Folders API
  slug: wegalvanize-robots-folders-api
- description: Folder's collaborators are users who have access to all the robots in that folder.
  name: Wegalvanize Robots Folders Collaborators API
  slug: wegalvanize-robots-folders-collaborators-api
- description: Get the hours a user is currently scheduled for. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=pm-schedule-resources" target="_blank">Learn more</a>.
  name: Wegalvanize Scheduled Hours API
  slug: wegalvanize-scheduled-hours-api
- description: Get the list of projects a user is scheduled for, and the projects' start and end dates. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=pm-schedule-resources" target="_bl
  name: Wegalvanize Scheduled Projects API
  slug: wegalvanize-scheduled-projects-api
- description: Get a list of all of the users currently scheduled for a project. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=pm-schedule-resources" target="_blank">Learn more</a>.
  name: Wegalvanize Scheduled Users API
  slug: wegalvanize-scheduled-users-api
- description: Sign-off on work you have prepared or reviewed, and assign another person as the next reviewer <a href="https://help.highbond.com/helpdocs/highbond/en-us/Content/projects/fieldwork/reviews/reviewing_w
  name: Wegalvanize Sign-offs API
  slug: wegalvanize-sign-offs-api
- description: A storyboard is a communication platform that displays multiple visualizations and rich text content in rows and columns. You can use this API to create, configure, update, and delete storyboards. How
  name: Wegalvanize Storyboards API
  slug: wegalvanize-storyboards-api
- description: You can use the Strategy app to identify, assess, and monitor strategic risks. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Content/strategy/landing_pages/user_guide.htm" target="_blank"
  name: Wegalvanize Strategy API
  slug: wegalvanize-strategy-api
- description: The Surveys API from Wegalvanize — 2 operation(s) for surveys.
  name: Wegalvanize Surveys API
  slug: wegalvanize-surveys-api
- description: A group of columns defines a table's schema. A column's `field_name` must be unique within a table, follow the <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=rm-import-ex
  name: Wegalvanize Table columns API
  slug: wegalvanize-table-columns-api
- description: 'Tables store records of data in rows and columns. They are a third level of organization in Results. Each table lives in an analysis, which lives in a collection. Your organization can have a maximum '
  name: Wegalvanize Tables API
  slug: wegalvanize-tables-api
- description: Use time entries to record time spent on projects, or on other tasks, for reporting purposes. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=pm-managing-timesheets" targe
  name: Wegalvanize Time entries API
  slug: wegalvanize-time-entries-api
- description: To-dos are a collaboration tool between teammates and reviewers. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Content/projects/fieldwork/reviews/assigning_to-dos.html" target="_blank">Le
  name: Wegalvanize To-dos API
  slug: wegalvanize-to-dos-api
- description: A user represents a member of HighBond. Users can belong to multiple instances. <a href="https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=lp-adding-users" target="_blank">Learn more
  name: Wegalvanize Users API
  slug: wegalvanize-users-api
- description: 'A walkthrough is a series of steps you perform to establish the reliability of controls and test the design of controls. Each control you define has a corresponding walkthrough that is used to verify '
  name: Wegalvanize Walkthroughs API
  slug: wegalvanize-walkthroughs-api
- description: Workflow groups are a permissions feature that allow you to define users as members of a specific group. A single user can belong to multiple workflow groups. <a href="https://help.highbond.com/helpdo
  name: Wegalvanize Workflow Groups API
  slug: wegalvanize-workflow-groups-api
- description: Workflows contain a set of statuses that a certain item belonging to that workflow can be in. Any items in this workflow can move between certain statuses and the transition can trigger certain events
  name: Wegalvanize Workflows in Asset Inventory/Asset Manager API
  slug: wegalvanize-workflows-in-asset-inventory-asset-manager-api
artifact_total: 144
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HighBond API Reference Actions API
  slug: open-wegalvanize-actions-api
- collection_type: open
  name: HighBond API Reference Actions Activities API
  slug: open-wegalvanize-activities-api
- collection_type: open
  name: HighBond API Reference Actions Analyses API
  slug: open-wegalvanize-analyses-api
- collection_type: open
  name: HighBond API Reference Actions Attachments API
  slug: open-wegalvanize-attachments-api
- collection_type: open
  name: HighBond API Reference Actions Collaborators API
  slug: open-wegalvanize-collaborators-api
- collection_type: open
  name: HighBond API Reference Actions Collections API
  slug: open-wegalvanize-collections-api
- collection_type: open
  name: HighBond API Reference Actions Compliance Maps API
  slug: open-wegalvanize-compliance-maps-api
- collection_type: open
  name: HighBond API Reference Actions Control performance schedules API
  slug: open-wegalvanize-control-performance-schedules-api
- collection_type: open
  name: HighBond API Reference Actions Control test plans API
  slug: open-wegalvanize-control-test-plans-api
- collection_type: open
  name: HighBond API Reference Actions Control tests API
  slug: open-wegalvanize-control-tests-api
- collection_type: open
  name: HighBond API Reference Actions Controls API
  slug: open-wegalvanize-controls-api
- collection_type: open
  name: HighBond API Reference Actions Custom attributes API
  slug: open-wegalvanize-custom-attributes-api
- collection_type: open
  name: HighBond API Reference Actions Entities API
  slug: open-wegalvanize-entities-api
- collection_type: open
  name: HighBond API Reference Actions Event Reports API
  slug: open-wegalvanize-event-reports-api
- collection_type: open
  name: HighBond API Reference Actions Events API
  slug: open-wegalvanize-events-api
- collection_type: open
  name: HighBond API Reference Actions Extract API
  slug: open-wegalvanize-extract-api
- collection_type: open
  name: HighBond API Reference Actions Flow Key API
  slug: open-wegalvanize-flow-key-api
- collection_type: open
  name: HighBond API Reference Actions Frameworks API
  slug: open-wegalvanize-frameworks-api
- collection_type: open
  name: HighBond API Reference Actions Groups API
  slug: open-wegalvanize-groups-api
- collection_type: open
  name: HighBond API Reference Actions Handlers API
  slug: open-wegalvanize-handlers-api
- collection_type: open
  name: HighBond API Reference Actions Importer API
  slug: open-wegalvanize-importer-api
- collection_type: open
  name: HighBond API Reference Actions Interpretations API
  slug: open-wegalvanize-interpretations-api
- collection_type: open
  name: HighBond API Reference Actions Issues API
  slug: open-wegalvanize-issues-api
- collection_type: open
  name: HighBond API Reference Actions Metrics API
  slug: open-wegalvanize-metrics-api
- collection_type: open
  name: HighBond API Reference Actions Mitigations API
  slug: open-wegalvanize-mitigations-api
- collection_type: open
  name: HighBond API Reference Actions Narratives API
  slug: open-wegalvanize-narratives-api
- collection_type: open
  name: HighBond API Reference Actions Non-project time categories API
  slug: open-wegalvanize-non-project-time-categories-api
- collection_type: open
  name: HighBond API Reference Actions Objectives API
  slug: open-wegalvanize-objectives-api
- collection_type: open
  name: HighBond API Reference Actions Planning files API
  slug: open-wegalvanize-planning-files-api
- collection_type: open
  name: HighBond API Reference Actions Project types API
  slug: open-wegalvanize-project-types-api
- collection_type: open
  name: HighBond API Reference Actions Projects API
  slug: open-wegalvanize-projects-api
- collection_type: open
  name: HighBond API Reference Actions Questionnaires API
  slug: open-wegalvanize-questionnaires-api
- collection_type: open
  name: HighBond API Reference Actions Record columns API
  slug: open-wegalvanize-record-columns-api
- collection_type: open
  name: HighBond API Reference Actions Record statuses API
  slug: open-wegalvanize-record-statuses-api
- collection_type: open
  name: HighBond API Reference Actions Records API
  slug: open-wegalvanize-records-api
- collection_type: open
  name: HighBond API Reference Actions Request item statuses API
  slug: open-wegalvanize-request-item-statuses-api
- collection_type: open
  name: HighBond API Reference Actions Request Items API
  slug: open-wegalvanize-request-items-api
- collection_type: open
  name: HighBond API Reference Actions Results files API
  slug: open-wegalvanize-results-files-api
- collection_type: open
  name: HighBond API Reference Actions Results Triggers API
  slug: open-wegalvanize-results-triggers-api
- collection_type: open
  name: HighBond API Reference Actions Results Users API
  slug: open-wegalvanize-results-users-api
- collection_type: open
  name: HighBond API Reference Actions Risks API
  slug: open-wegalvanize-risks-api
- collection_type: open
  name: HighBond API Reference Actions Robot Activations API
  slug: open-wegalvanize-robot-activations-api
- collection_type: open
  name: HighBond API Reference Actions Robot Apps API
  slug: open-wegalvanize-robot-apps-api
- collection_type: open
  name: HighBond API Reference Actions Robot Collaborators API
  slug: open-wegalvanize-robot-collaborators-api
- collection_type: open
  name: HighBond API Reference Actions Robot Files API
  slug: open-wegalvanize-robot-files-api
- collection_type: open
  name: HighBond API Reference Actions Robot Jobs API
  slug: open-wegalvanize-robot-jobs-api
- collection_type: open
  name: HighBond API Reference Actions Robot Script Versions API
  slug: open-wegalvanize-robot-script-versions-api
- collection_type: open
  name: HighBond API Reference Actions Robot Tasks API
  slug: open-wegalvanize-robot-tasks-api
- collection_type: open
  name: HighBond API Reference Actions Robot Users API
  slug: open-wegalvanize-robot-users-api
- collection_type: open
  name: HighBond API Reference Actions Robot Working Files API
  slug: open-wegalvanize-robot-working-files-api
- collection_type: open
  name: HighBond API Reference Actions Robots Agents API
  slug: open-wegalvanize-robots-agents-api
- collection_type: open
  name: HighBond API Reference Actions Robots API
  slug: open-wegalvanize-robots-api
- collection_type: open
  name: HighBond API Reference Actions Robots Folders API
  slug: open-wegalvanize-robots-folders-api
- collection_type: open
  name: HighBond API Reference Actions Robots Folders Collaborators API
  slug: open-wegalvanize-robots-folders-collaborators-api
- collection_type: open
  name: HighBond API Reference Actions Scheduled Hours API
  slug: open-wegalvanize-scheduled-hours-api
- collection_type: open
  name: HighBond API Reference Actions Scheduled Projects API
  slug: open-wegalvanize-scheduled-projects-api
- collection_type: open
  name: HighBond API Reference Actions Scheduled Users API
  slug: open-wegalvanize-scheduled-users-api
- collection_type: open
  name: HighBond API Reference Actions Sign-offs API
  slug: open-wegalvanize-sign-offs-api
- collection_type: open
  name: HighBond API Reference Actions Storyboards API
  slug: open-wegalvanize-storyboards-api
- collection_type: open
  name: HighBond API Reference Actions Strategy API
  slug: open-wegalvanize-strategy-api
- collection_type: open
  name: HighBond API Reference Actions Surveys API
  slug: open-wegalvanize-surveys-api
- collection_type: open
  name: HighBond API Reference Actions Table columns API
  slug: open-wegalvanize-table-columns-api
- collection_type: open
  name: HighBond API Reference Actions Tables API
  slug: open-wegalvanize-tables-api
- collection_type: open
  name: HighBond API Reference Actions Time entries API
  slug: open-wegalvanize-time-entries-api
- collection_type: open
  name: HighBond API Reference Actions To-dos API
  slug: open-wegalvanize-to-dos-api
- collection_type: open
  name: HighBond API Reference Actions Users API
  slug: open-wegalvanize-users-api
- collection_type: open
  name: HighBond API Reference Actions Walkthroughs API
  slug: open-wegalvanize-walkthroughs-api
- collection_type: open
  name: HighBond API Reference Actions Workflow Groups API
  slug: open-wegalvanize-workflow-groups-api
- collection_type: open
  name: HighBond API Reference Actions Workflows in Asset Inventory/Asset Manager API
  slug: open-wegalvanize-workflows-in-asset-inventory-asset-manager-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/diligent-boards/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wegalvanize-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wegalvanize-highbond-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wegalvanize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wegalvanize.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs-apis.highbond.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.highbond.com/helpdocs/highbond/en-us/Default.htm
- group: docs
  title: ''
  type: APIReference
  url: https://docs-apis.highbond.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.highbond.com/helpdocs/highbond/en-us/Default.htm#cshid=lp-access-tokens
- group: auth
  title: ''
  type: Authentication
  url: authentication/wegalvanize-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wegalvanize-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wegalvanize-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wegalvanize-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wegalvanize-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.diligent.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/wegalvanize-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wegalvanize-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.diligent.com
- group: design
  title: ''
  type: DataModel
  url: data-model/wegalvanize-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wegalvanize-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wegalvanize-well-known.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/diligentcorp
- group: operate
  title: ''
  type: Support
  url: https://help.highbond.com/helpdocs/highbond/en-us/Default.htm
- group: start
  title: ''
  type: Login
  url: https://www.highbond.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.diligent.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diligent.com/privacy
created: '2026-07-17'
description: Wegalvanize.com is the former web home of Galvanize, the governance, risk, and compliance (GRC) software company behind the HighBond platform; Galvanize was acquired by Diligent and wegalvanize.com now redirects to diligent.com. The HighBond platform (audit, risk, controls, compliance, data analytics, and Robots automation) exposes a substantial public REST API built on the JSON:API v1.0 specification, documented at docs-apis.highbond.com and authenticated with OAuth 2.0 bearer tokens issued through Launchpad. This profile was seeded as a Norwest Venture Partners portfolio lead and has been enriched from the live HighBond OpenAPI (390 operations across 67 resource groups) and the provider's public identity/security surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wegalvanize.png
layout: provider
mcp_servers:
- description: ''
  name: Wegalvanize MCP Server
  slug: wegalvanize-mcp-server
modified: '2026-07-21'
name: Wegalvanize
nav: Providers
network: true
overview: 'Wegalvanize publishes 69 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Activities API, Analyses API, and 66 more. Tagged areas include Company, Governance, Risk, Compliance, and Audit.


  Wegalvanize''s developer surface includes documentation, API reference, getting-started guide, authentication, support, and 22 more developer resources.'
random_paper: 5
scopes:
- name: Wegalvanize Scopes
  scope_count: 7
  slug: wegalvanize-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials/implicit/refreshToken/tokenExchange
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 52.5
    developer_ergonomics: 56.5
    discoverability: 63.0
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 42.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 69
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wegalvanize/refs/heads/main/screenshots/wegalvanize-2026-08-17T082923.png
security:
- kind: authentication
  name: Wegalvanize Authentication
  slug: wegalvanize-authentication
  summary_line: http/oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Wegalvanize Domain Security
  slug: wegalvanize-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Wegalvanize Trust Center
  slug: wegalvanize-trust-center
  summary_line: SOC 1, SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: wegalvanize
tags:
- Company
- Governance
- Risk
- Compliance
- Audit
- GRC
- Analytics
- Automation
- Security
website: https://wegalvanize.com
---
