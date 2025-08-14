---
aid: climatiq
url: >-
  https://raw.githubusercontent.com/api-evangelist/climatiq/refs/heads/main/apis.yml
apis:
  - aid: climatiq:search-api
    name: Climatiq Search API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/search
    properties:
      - url: https://www.climatiq.io/docs/api-reference/search
        type: Documentation
    description: >-
      GET Allows you to determine what emission factors are available to be used
      in your estimates.
  - aid: climatiq:intermodal-freight-v2-api
    name: Climatiq Intermodal Freight v2 API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/intermodal-freight
    properties:
      - url: https://www.climatiq.io/docs/api-reference/intermodal-freight
        type: Documentation
    description: >-
      Climatiq allows you to use emission factors from the Global Logistics
      Emissions Council(GLEC)(opens in a new tab) to calculate the carbon
      emissions for shipping freight around the world using multiple modes of
      transport such as by sea, air, road or rail.
  - aid: climatiq:travel-api
    name: Climatiq Travel API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/travel
    properties:
      - url: https://www.climatiq.io/docs/api-reference/travel
        type: Documentation
    description: >-
      Climatiq provides a comprehensive toolkit to help businesses measure GHG
      emissions from travel activities. This includes reporting scope 3.6
      emissions under the GHG Protocol for travel activities in vehicles owned
      or operated by third parties, such as aircraft, trains and passenger cars.
      Emissions associated with hotel stays can also be calculated, providing a
      comprehensive view of travel-related emissions.
  - aid: climatiq:classifications-api
    name: Climatiq Classifications API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/classifications
    properties:
      - url: https://www.climatiq.io/docs/api-reference/classifications
        type: Documentation
    description: >-
      Many sources link emission factors(opens in a new tab) to specific
      industry classification schemes, and Climatiq makes it possible to select
      an emission factor based on these industry classification codes. Please
      see below the list of mappings we currently support, with the datasets
      that are mapped directly to them (note that the API will also map factors
      indirectly via the UN correspondence tables(opens in a new tab)):
  - aid: climatiq:energy-v1-api
    name: Climatiq Energy v1 API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/energy
    properties:
      - url: https://www.climatiq.io/docs/api-reference/energy
        type: Documentation
    description: >-
      The energy endpoints automatically calculates the greenhouse gas emissions
      associated with the consumed energy based on relevant emission factors.
      These factors are determined based on the specific type of energy and the
      region where it is consumed, ensuring accurate carbon footprint
      calculations for your organization.
  - aid: climatiq:autopilot-api
    name: Climatiq Autopilot API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/autopilot
    properties:
      - url: https://www.climatiq.io/docs/api-reference/autopilot
        type: Documentation
    description: >-
      Autopilot is an AI-powered calculation endpoint designed to automate
      spend- and activity-based emission estimates. It uses a proprietary
      natural language processing (NLP) model paired with Climatiqs scientific
      expertise to streamline complex emission calculations, making carbon
      insights accessible to non-experts.
  - aid: climatiq:estimation-api
    name: Climatiq Estimation API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/estimate
    properties:
      - url: https://www.climatiq.io/docs/api-reference/estimate
        type: Documentation
    description: >-
      Estimation operations are performed to calculate emissions produced by one
      or more activities, based on multiplying activity data by the appropriate
      emission factors.
  - aid: climatiq:cloud-computing-api
    name: Climatiq Cloud Computing API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/computing
    properties:
      - url: https://www.climatiq.io/docs/api-reference/computing
        type: Documentation
    description: >-
      Climatiq makes endpoints available to help you calculate the carbon
      footprint of the cloud resources you use. It will automatically select
      emission factors based on your cloud provider and region, so you get the
      right emission factor for your datacenter.
  - aid: climatiq:procurement-api
    name: Climatiq Procurement API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/procurement
    properties:
      - url: https://www.climatiq.io/docs/api-reference/procurement
        type: Documentation
    description: >-
      Spend-based estimations enable carbon footprint calculations for purchased
      goods and services (GHG Protocol Category 3.1) using expenditure data.
      They are especially valuable when precise activity data is not readily
      available.
  - aid: climatiq:custom-mappings-api
    name: Climatiq Custom Mappings API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/custom-mappings
    properties:
      - url: https://www.climatiq.io/docs/api-reference/custom-mappings
        type: Documentation
    description: >-
      Instead of using code to specify emission factors you want to use for your
      calculations, you can map your own labels to Climatiq activity IDs in the
      Climatiq dashboard(opens in a new tab), allowing the Climatiq API to
      recognize whatever values you use to categorize your activities. In the
      dashboard simply link a custom mapping label to an activity ID, and this
      can then be used in the custom mapping endpoints.
  - aid: climatiq:carbon-border-adjustment-mechanism-api
    name: Climatiq Carbon Border Adjustment Mechanism API
    tags: []
    humanURL: https://www.climatiq.io/docs/api-reference/cbam
    properties:
      - url: https://www.climatiq.io/docs/api-reference/cbam
        type: Documentation
    description: >-
      The Carbon Border Adjustment Mechanism (CBAM)(opens in a new tab) has been
      introduced by the European Union (EU) to promote lower carbon production
      in countries outside of the EU. It places requirements on importers of
      certain goods (currently Iron 
name: Climatiq
tags:
  - Environment
  - Data
  - Energy
  - Waste
  - Carbon Emissions
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.climatiq.io/
    name: Climatiq - API for Carbon Footprint Calculations
    type: Website
    description: 'null'
  - url: https://www.climatiq.io/pricing
    name: Pricing and Plans | Climatiq API
    type: Pricing
    description: 'null'
  - url: https://www.climatiq.io/blog
    name: Climatiq Blog
    type: Blog
    description: 'null'
  - url: https://trust.climatiq.io/
    name: Trust Center - Climatiq
    type: Trust
    description: 'null'
  - url: https://www.climatiq.io/support
    name: Support
    type: Support
    description: 'null'
  - url: https://www.climatiq.io/customers
    name: Customer Stories | Climatiq
    type: Customers
    description: 'null'
  - url: https://auth.climatiq.io/login
    name: Sign In with Climatiq
    type: Login
    description: 'null'
  - url: https://www.climatiq.io/demo
    name: API Demo - Climatiq
    type: Playground
    description: 'null'
  - url: https://www.climatiq.io/partner-with-climatiq
    name: Partner with Climatiq
    type: Partners
    description: 'null'
  - url: https://www.climatiq.io/newsletter
    name: Subscribe to our Newsletter
    type: Newsletter
    description: 'null'
  - url: https://www.climatiq.io/docs/guides/tutorials/quickstart
    name: >-
      Quickstart - Climatiq How-To Guides - Automated Carbon Emission
      Calculations
    type: GettingStarted
    description: 'null'
  - url: https://www.climatiq.io/docs/changelogs/api-release
    name: API Versions - Automated Carbon Emission Calculations
    type: Versioning
    description: 'null'
created: '2025-02-24'
modified: '2025-02-27'
position: Consumer
description: >-
  Climatiq is a data analytics company that specializes in providing businesses
  with insights into their environmental impact. By collecting and analyzing
  data related to energy consumption, waste production, and carbon emissions,
  Climatiq helps companies identify opportunities to reduce their environmental
  footprint and make more sustainable choices. Through the use of cutting-edge
  technology and innovative solutions, Climatiq empowers organizations to take
  actionable steps towards a greener future while also improving their bottom
  line.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---