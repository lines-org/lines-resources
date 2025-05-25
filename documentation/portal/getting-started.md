# Getting Started with the LineS Portal

## Setting up an account

To create and edit feeds, you need to create an account in the LineS Portal.

- Click the `Login` button in the top right corner and then click `Sign Up` to create a new account.
- Insert your email address and a strong password. You will receive a confirmation email.
- Click the link in the email to activate your account and automatically log in to the portal. 

## Your account

You can manage your account by clicking the `User Icon` in the top right corner and selecting `Account` from the dropdown menu.

- **Change password -** You can change your password at any time. You need to be logged in to change your password.

- **Manage API key -** You can (re)generate and copy your API key. This key is used to authenticate your requests to the Feeds API. Keep it secure and do not share it with anyone! 
  
You can log out of your account by clicking the `User Icon` in the top right corner and selecting `Logout` from the dropdown menu.

## Exploring the dashboard

You can access your dashboard in two different ways.

- Click the `Dashboard` in the top navigation bar.
- Click the `User Icon` in the top right corner and select `Dashboard` from the dropdown menu.

The dashboard allows you to manage your feeds in a single place. 

- **Create a feed -** You must provide a unique ID for your feed, a name for it, and optionally a description. The feed ID will be used to identify your feed in the Feeds API.
  - You will be able to edit the name and description of your feed later, as well as remove it. You are the only one who can perform these actions.

- **Add a feed editor -** You can add other users as editors of your feeds by providing their email addresses.
  - Editors can edit the feed in the Feeds API, but they cannot delete it or add other editors. You can remove editors at any time.

- **View feeds shared with you -** This section shows the feeds you can edit. It displays the feeds other users have shared with you.

- **Manage API key -** You can (re)generate and copy your API key. This key is used to authenticate your requests to the Feeds API. Keep it secure and do not share it with anyone!

## View available feeds

You can view all the available feeds in the LineS Portal. Click the `Feeds` link in the top navigation bar to access the feeds page.

If you click to see the details of a feed, you can see the following information.

- **View feed metadata -** The feed metadata includes the feed ID, name, description, and the date it was created.

- **Download feed -** You can download the feed by clicking the `Download` button. The file will follow the GTFS specification, that is, a ZIP file containing CSV files with the feed data.

- **Show report -** You can generate a report of the feed using the Canonical GTFS Schedule Validator. The results will be displayed in the page in order to help you identify any issues with the feed.

- **View change log -** You can view the change log of the feed, which shows the history of changes made to the feed, and who made them.

- **View commit diffs -** You can view the changes introduced by each commit in the change log. It will show you the difference between the selected commit and the previous one, highlighting the changes made to the feed files.

Additionally, if you are an editor of the feed, you can perform the following actions.

- **Upload feed -** You can upload a new version of the feed by clicking the `Upload` button or dragging it into the respective boxed area. The file must be a ZIP file following the GTFS specification.

- **Revert a commit -** You can revert a specific commit by clicking the `Revert` button next to the commit in the change log. This will create a new commit that reverts the changes made in the selected commit.

## Read the documentation

You can read the documentation of the LineS Portal by clicking the `Documentation` link in the top navigation bar.

The documentation provides detailed information on how to use the portal and the Feeds API. It includes guides on how to create and manage feeds, examples of how to use the API programmatically, along with a toolkit to help you get started.