digraph model_graph {
  // Dotfile by Django-Extensions graph_models
  // Created: 2023-02-28 12:09
  // Cli Options: -a -g --dot -o engenhariadesoftware/20230228/engenhariadesoftwaredesembola.dot

  fontname = "Roboto"
  fontsize = 8
  splines  = true

  node [
    fontname = "Roboto"
    fontsize = 8
    shape = "plaintext"
  ]

  edge [
    fontname = "Roboto"
    fontsize = 8
  ]

  // Labels
  subgraph cluster_django_contrib_admin {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.admin</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    django_contrib_admin_models_LogEntry [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      LogEntry
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>content_type</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">action_flag</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveSmallIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">action_time</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">change_message</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">object_id</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">object_repr</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_django_contrib_auth {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.auth</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    django_contrib_auth_models_AbstractUser [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      AbstractUser<BR/>&lt;<FONT FACE="Roboto"><I>AbstractBaseUser,PermissionsMixin</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">date_joined</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">email</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">EmailField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">first_name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_active</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_staff</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_superuser</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_login</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">last_name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>password</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">username</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_contrib_auth_models_Permission [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Permission
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>content_type</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">codename</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_contrib_auth_models_Group [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Group
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_contrib_auth_models_User [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      User<BR/>&lt;<FONT FACE="Roboto"><I>AbstractUser</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>date_joined</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>email</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>EmailField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>first_name</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_active</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_staff</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_superuser</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_login</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_name</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>password</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>username</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_django_contrib_contenttypes {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.contenttypes</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    django_contrib_contenttypes_models_ContentType [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      ContentType
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">app_label</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">model</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_django_contrib_sessions {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.sessions</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    django_contrib_sessions_base_session_AbstractBaseSession [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      AbstractBaseSession
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">expire_date</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">session_data</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_contrib_sessions_models_Session [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Session<BR/>&lt;<FONT FACE="Roboto"><I>AbstractBaseSession</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I><B>session_key</B></I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I><B>CharField</B></I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>expire_date</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>session_data</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>TextField</I></FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_newsfeed {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>newsfeed</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    newsfeed_models_Issue [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Issue
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">created_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_draft</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">issue_number</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">issue_type</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveSmallIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">publish_date</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">short_description</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">title</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">updated_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    newsfeed_models_PostCategory [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      PostCategory
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">order</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    newsfeed_models_Post [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Post
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>category</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>issue</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">created_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_visible</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">order</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">short_description</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">RichTextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">source_url</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">URLField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">tempo_de_leitura</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">title</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">updated_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    newsfeed_models_Newsletter [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Newsletter
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>issue</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">created_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_sent</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">schedule</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">sent_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">subject</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">updated_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    newsfeed_models_Subscriber [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Subscriber
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">created_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">email_address</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">EmailField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">subscribed</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">token</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">verification_sent_date</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">verified</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_django_celery_beat {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django_celery_beat</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    django_celery_beat_models_SolarSchedule [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      SolarSchedule
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">event</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">latitude</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DecimalField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">longitude</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DecimalField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_celery_beat_models_IntervalSchedule [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      IntervalSchedule
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">every</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">IntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">period</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_celery_beat_models_ClockedSchedule [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      ClockedSchedule
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">clocked_time</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_celery_beat_models_CrontabSchedule [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      CrontabSchedule
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">day_of_month</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">day_of_week</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">hour</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">minute</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">month_of_year</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">timezone</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">TimeZoneField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_celery_beat_models_PeriodicTasks [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      PeriodicTasks
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>ident</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>SmallIntegerField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">last_update</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    django_celery_beat_models_PeriodicTask [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      PeriodicTask
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>clocked</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>crontab</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>interval</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>solar</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">args</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">date_changed</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">description</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">enabled</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">exchange</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">expire_seconds</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">expires</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">headers</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">kwargs</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">last_run_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">one_off</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">priority</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">queue</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">routing_key</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">start_time</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">task</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">total_run_count</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_easy_thumbnails {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>easy_thumbnails</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    easy_thumbnails_models_File [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      File
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">modified</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">storage_hash</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    easy_thumbnails_models_Source [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Source<BR/>&lt;<FONT FACE="Roboto"><I>File</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>modified</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>name</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>storage_hash</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    easy_thumbnails_models_Thumbnail [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Thumbnail<BR/>&lt;<FONT FACE="Roboto"><I>File</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>source</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>modified</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>name</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>storage_hash</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    easy_thumbnails_models_ThumbnailDimensions [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      ThumbnailDimensions
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>thumbnail</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>OneToOneField (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">height</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">width</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveIntegerField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_comercial_4_0 {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>comercial_4_0</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    comercial_4_0_models_Produto [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Produto
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    comercial_4_0_models_Vendedor [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Vendedor
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    comercial_4_0_models_Clientes [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Clientes
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">comercial_type</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveSmallIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">created_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">descricao_do_cliente</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">RichTextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">endereco_de_email</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">EmailField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">updated_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    comercial_4_0_models_Comercial_Pre_Venda [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Comercial_Pre_Venda
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    comercial_4_0_models_Comercial_Venda [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Comercial_Venda
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    comercial_4_0_models_Comercial_Pos_Venda [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Comercial_Pos_Venda
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    comercial_4_0_models_Vendas [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Vendas
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>nome_produto</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>vendedor</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">data</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">total</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">FloatField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_financeiro {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>financeiro</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    financeiro_models_Gastos_e_Ganhos [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Gastos_e_Ganhos
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    financeiro_models_Professor [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Professor
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]
  
    financeiro_models_Total [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Total
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>nome_total</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>professor</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">data</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">total</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">FloatField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }
  subgraph cluster_tarefas {
    label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>tarefas</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >
    color=olivedrab4
    style="rounded"
  
    tarefas_models_Tarefas [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Tarefas
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">created_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">descricao_da_tarefa</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nome</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">realizada</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">updated_at</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >]

  }


  // Relations

  django_contrib_admin_models_LogEntry -> django_contrib_auth_models_User
  [label=" user (logentry)"] [arrowhead=none, arrowtail=dot, dir=both];

  django_contrib_admin_models_LogEntry -> django_contrib_contenttypes_models_ContentType
  [label=" content_type (logentry)"] [arrowhead=none, arrowtail=dot, dir=both];

  django_contrib_auth_base_user_AbstractBaseUser [label=<
  <TABLE BGCOLOR="white" BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="#1b563f">
  <FONT FACE="Roboto" POINT-SIZE="12" COLOR="white">AbstractBaseUser</FONT>
  </TD></TR>
  </TABLE>
  >]
  django_contrib_auth_models_AbstractUser -> django_contrib_auth_base_user_AbstractBaseUser
  [label=" abstract\ninheritance"] [arrowhead=empty, arrowtail=none, dir=both];
  django_contrib_auth_models_PermissionsMixin [label=<
  <TABLE BGCOLOR="white" BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="#1b563f">
  <FONT FACE="Roboto" POINT-SIZE="12" COLOR="white">PermissionsMixin</FONT>
  </TD></TR>
  </TABLE>
  >]
  django_contrib_auth_models_AbstractUser -> django_contrib_auth_models_PermissionsMixin
  [label=" abstract\ninheritance"] [arrowhead=empty, arrowtail=none, dir=both];

  django_contrib_auth_models_Permission -> django_contrib_contenttypes_models_ContentType
  [label=" content_type (permission)"] [arrowhead=none, arrowtail=dot, dir=both];

  django_contrib_auth_models_Group -> django_contrib_auth_models_Permission
  [label=" permissions (group)"] [arrowhead=dot arrowtail=dot, dir=both];

  django_contrib_auth_models_User -> django_contrib_auth_models_Group
  [label=" groups (user)"] [arrowhead=dot arrowtail=dot, dir=both];

  django_contrib_auth_models_User -> django_contrib_auth_models_Permission
  [label=" user_permissions (user)"] [arrowhead=dot arrowtail=dot, dir=both];

  django_contrib_auth_models_User -> django_contrib_auth_models_AbstractUser
  [label=" abstract\ninheritance"] [arrowhead=empty, arrowtail=none, dir=both];



  django_contrib_sessions_models_Session -> django_contrib_sessions_base_session_AbstractBaseSession
  [label=" abstract\ninheritance"] [arrowhead=empty, arrowtail=none, dir=both];


  newsfeed_models_Post -> newsfeed_models_Issue
  [label=" issue (posts)"] [arrowhead=none, arrowtail=dot, dir=both];

  newsfeed_models_Post -> newsfeed_models_PostCategory
  [label=" category (posts)"] [arrowhead=none, arrowtail=dot, dir=both];

  newsfeed_models_Newsletter -> newsfeed_models_Issue
  [label=" issue (newsletters)"] [arrowhead=none, arrowtail=dot, dir=both];


  django_celery_beat_models_PeriodicTask -> django_celery_beat_models_IntervalSchedule
  [label=" interval (periodictask)"] [arrowhead=none, arrowtail=dot, dir=both];

  django_celery_beat_models_PeriodicTask -> django_celery_beat_models_CrontabSchedule
  [label=" crontab (periodictask)"] [arrowhead=none, arrowtail=dot, dir=both];

  django_celery_beat_models_PeriodicTask -> django_celery_beat_models_SolarSchedule
  [label=" solar (periodictask)"] [arrowhead=none, arrowtail=dot, dir=both];

  django_celery_beat_models_PeriodicTask -> django_celery_beat_models_ClockedSchedule
  [label=" clocked (periodictask)"] [arrowhead=none, arrowtail=dot, dir=both];


  easy_thumbnails_models_Source -> easy_thumbnails_models_File
  [label=" abstract\ninheritance"] [arrowhead=empty, arrowtail=none, dir=both];

  easy_thumbnails_models_Thumbnail -> easy_thumbnails_models_Source
  [label=" source (thumbnails)"] [arrowhead=none, arrowtail=dot, dir=both];

  easy_thumbnails_models_Thumbnail -> easy_thumbnails_models_File
  [label=" abstract\ninheritance"] [arrowhead=empty, arrowtail=none, dir=both];

  easy_thumbnails_models_ThumbnailDimensions -> easy_thumbnails_models_Thumbnail
  [label=" thumbnail (dimensions)"] [arrowhead=none, arrowtail=none, dir=both];


  comercial_4_0_models_Vendas -> comercial_4_0_models_Produto
  [label=" nome_produto (vendas)"] [arrowhead=none, arrowtail=dot, dir=both];

  comercial_4_0_models_Vendas -> comercial_4_0_models_Vendedor
  [label=" vendedor (vendas)"] [arrowhead=none, arrowtail=dot, dir=both];


  financeiro_models_Total -> financeiro_models_Gastos_e_Ganhos
  [label=" nome_total (total)"] [arrowhead=none, arrowtail=dot, dir=both];

  financeiro_models_Total -> financeiro_models_Professor
  [label=" professor (total)"] [arrowhead=none, arrowtail=dot, dir=both];



}
