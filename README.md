# Hospital_Management_System
This application helps in managin basic hospital services online


## Project Description

As the first step patient will register in the application to the specific hospital. After registering patient will be asked to login into their accounts which is quite common thing. After login patients will be redirected to their dashboards from where they can access their medicines and also bills. 
From the dashboard patient will be applied to the opcard if not issued. If opcard is already issued, then there will be option to again book appointment. 
On the other hand, Hospital and medicine logins will be created by application admin which can be created at the time of development. 
Hospital will login to their dashboards and after that there will be list of patients who created opcards or booked appointments. Whenever patient booked appointment of created opcard then it will get reflected here and hospital management can see patient details in the table format. 
From this dashboard receptionist can add temperature to the patient and allows him to meet doctor. When doctor has completed checking he then give suggestions to patient and assign medicines for him form the same dashboard.
Medicine staff on the other hand will login to their accounts and be ready for the patients. Whenever doctor assigned medicines for the user those medicine swill be reflected in the medicine dashboard. It will have patient details and medicine names of that patient. 
From here medicine staff will give that prescribed medicines to that patient and mark the status as paid after collecting the money. This will mark the patient as paid the bill and also record his bills and medicines.
At last after completion patient can be able to see his/her bills in the bills section of their dashboard and medicines in the medicines section of their dashboard. Those will be updated whenever patient visits the hospital.


## Architecture

Coming to architecture it describes the steps we need to complete in the project and we have used Coggle to draw the architectures and also other images.

<img src="https://drive.google.com/uc?export=view&id=1fDwzsYLb08Tgczwn-kjTBwIgdXddF9W_"/>
 
Fig : *Architecture of system*

We have used Coggle to draw the architecture of this project which is nothing but the steps to be followed while developing this project. As the first step we go for creating Authentication module which deals users authentication like registering and logging into the application.
They will be secured using a login ID and password which should be kept secretly and cannot be compromised. These logins are of 4 types mainly patient login, which is associated with the patient, hospital login, which is associated with the hospital and it will be created by the super admin.
Third one is medicine login, which is associated with the medicine staff and it will also be created by super admin. At last super admin login which will be create at the time of development.
All these logins are secured by unique login ID’s and passwords and no one cannot access others logins. Coming to next module, services which is used to manage services provided to user like op, bills and medicines. All these will be managed in this module.

<!-- ## Database Map

<img src="https://drive.google.com/uc?export=view&id=1Ce_CfcDOCEvbJAWzmznFVPl4hnqhRIV6"/>

## UI Screen Shots

UI screenshots             |  UI Screenshots
:-------------------------:|:-------------------------:
![image](https://drive.google.com/uc?export=view&id=1z5PVy0ubxMVFSy-jch5nlOTsJ4cEGigV)  |  ![image](https://drive.google.com/uc?export=view&id=1ufrVNdzxB1bMD91_XCZ0Ko92Qi2sNxrB)

### User Registration

<img src="https://drive.google.com/uc?export=view&id=1z5PVy0ubxMVFSy-jch5nlOTsJ4cEGigV"/>

### User Registration

<img src="https://drive.google.com/uc?export=view&id=1z5PVy0ubxMVFSy-jch5nlOTsJ4cEGigV"/>

### User Registration

<img src="https://drive.google.com/uc?export=view&id=1z5PVy0ubxMVFSy-jch5nlOTsJ4cEGigV"/>

### User Registration

<img src="https://drive.google.com/uc?export=view&id=1z5PVy0ubxMVFSy-jch5nlOTsJ4cEGigV"/>

### User Registration

<img src="https://drive.google.com/uc?export=view&id=1z5PVy0ubxMVFSy-jch5nlOTsJ4cEGigV"/>

### User Registration

<img src="https://drive.google.com/uc?export=view&id=1z5PVy0ubxMVFSy-jch5nlOTsJ4cEGigV"/>-->

