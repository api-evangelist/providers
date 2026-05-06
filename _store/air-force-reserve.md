---
aid: air-force-reserve
url: https://raw.githubusercontent.com/api-evangelist/air-force-reserve/refs/heads/main/apis.yml
name: Air Force Reserve
tags:
  - Federal Government
  - Military
  - Defense
  - Air Force
  - United States Government
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-04-19'
position: Consumer
description: The Air Force Reserve (AFRC) is the reserve component of the United States Air Force, headquartered at Robins Air Force Base, Georgia. It provides trained units and individuals to be available for active duty in time of war, national emergency, or when otherwise authorized by law. Air Force Reserve members serve part-time, typically one weekend per month and two weeks per year, while maintaining civilian careers. AFRC does not currently provide a public developer API but offers digital recruitment and informational resources.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: air-force-reserve:afrc
    name: Air Force Reserve Command
    tags:
      - Military
      - Defense
      - Reserve
      - Federal Government
      - Recruiting
    humanURL: https://www.afrc.af.mil/
    description: Air Force Reserve Command (AFRC) provides information on reserve programs, career opportunities, unit locations, benefits, and recruiting resources for prospective and current reservists.
    properties:
      - url: https://www.airforce.com/ways-to-serve/air-force-reserve
        type: Documentation
        title: Air Force Reserve Overview
      - url: https://www.afrc.af.mil/
        type: Website
        title: AFRC Official Website
      - url: https://www.airforce.com/apply-now
        type: Portal
        title: Application Portal
      - url: https://mypers.af.mil/
        type: Portal
        title: myPers Personnel System
common:
  - name: AFRC Official Website
    url: https://www.afrc.af.mil/
    type: Website
    description: Official Air Force Reserve Command website.
  - name: Air Force Reserve Recruiting
    url: https://www.airforce.com/ways-to-serve/air-force-reserve
    type: Portal
    description: Air Force Reserve recruiting portal with career opportunities and application resources.
  - name: myPers Personnel System
    url: https://mypers.af.mil/
    type: Portal
    description: Air Force personnel management system for assignments, records, and career management.
  - name: Air Force Portal
    url: https://www.my.af.mil/
    type: Portal
    description: Air Force portal for active and reserve members.
  - name: AFRC Privacy Policy
    url: https://www.afrc.af.mil/Privacy/
    type: PrivacyPolicy
    description: AFRC privacy and security policy for digital resources.
  - type: Features
    data:
      - name: Traditional Reserve Service
        description: Part-time service obligation of one weekend per month and 14 days per year with full access to Air Force training and benefits.
      - name: Active Guard Reserve (AGR)
        description: Full-time active-duty positions within the Reserve component with all active-duty benefits.
      - name: Individual Mobilization Augmentee (IMA)
        description: Reserve positions augmenting active-duty units during contingencies and deployments.
      - name: Air Reserve Technician (ART)
        description: Dual-status civilian/military positions serving as both federal civil servant and reserve member.
      - name: 200+ Career Fields
        description: Over 200 career specialties available across aviation, intelligence, cyber, medical, maintenance, and many other fields.
      - name: Educational Benefits
        description: Reserve Educational Assistance Program (REAP), GI Bill benefits, and tuition assistance for qualifying reservists.
      - name: Palace Chase/Front Programs
        description: Transition programs allowing active-duty airmen to transfer to the Reserve component.
      - name: Healthcare Benefits
        description: Access to TRICARE Reserve Select healthcare coverage for qualifying Reserve members and families.
  - type: UseCases
    data:
      - name: Reserve Recruiting
        description: Connect prospective members with available Air Force Reserve career opportunities and units.
      - name: Active Duty Transition
        description: Support active-duty airmen transitioning to Reserve status via Palace Chase/Front programs.
      - name: Unit Deployment Support
        description: Provide trained reserve units and individuals to augment active-duty missions during contingencies.
      - name: Cyber and Intelligence Missions
        description: Reserve cyber squadrons and intelligence units supporting national security missions part-time.
---
