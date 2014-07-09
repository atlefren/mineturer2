--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: mineturer; Type: SCHEMA; Schema: -; Owner: mineturer2
--

CREATE SCHEMA mineturer;


ALTER SCHEMA mineturer OWNER TO mineturer2;

SET search_path = mineturer, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: points; Type: TABLE; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

CREATE TABLE points (
    pid integer NOT NULL,
    tripid integer,
    ele double precision,
    "time" timestamp without time zone,
    geom public.geometry,
    hr double precision,
    CONSTRAINT enforce_dims_geom CHECK ((public.st_ndims(geom) = 2)),
    CONSTRAINT enforce_geotype_geom CHECK (((public.geometrytype(geom) = 'POINT'::text) OR (geom IS NULL))),
    CONSTRAINT enforce_srid_geom CHECK ((public.st_srid(geom) = 4326))
);


ALTER TABLE mineturer.points OWNER TO mineturer2;

--
-- Name: points_pid_seq; Type: SEQUENCE; Schema: mineturer; Owner: mineturer2
--

CREATE SEQUENCE points_pid_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE mineturer.points_pid_seq OWNER TO mineturer2;

--
-- Name: points_pid_seq; Type: SEQUENCE OWNED BY; Schema: mineturer; Owner: mineturer2
--

ALTER SEQUENCE points_pid_seq OWNED BY points.pid;


--
-- Name: routes; Type: TABLE; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

CREATE TABLE routes (
    routekid integer NOT NULL,
    tripid integer,
    geom public.geometry,
    CONSTRAINT enforce_dims_geom CHECK ((public.st_ndims(geom) = 2)),
    CONSTRAINT enforce_srid_geom CHECK ((public.st_srid(geom) = 4326))
);


ALTER TABLE mineturer.routes OWNER TO mineturer2;

--
-- Name: routes_routekid_seq; Type: SEQUENCE; Schema: mineturer; Owner: mineturer2
--

CREATE SEQUENCE routes_routekid_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE mineturer.routes_routekid_seq OWNER TO mineturer2;

--
-- Name: routes_routekid_seq; Type: SEQUENCE OWNED BY; Schema: mineturer; Owner: mineturer2
--

ALTER SEQUENCE routes_routekid_seq OWNED BY routes.routekid;


--
-- Name: tracks; Type: TABLE; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

CREATE TABLE tracks (
    trackid integer NOT NULL,
    tripid integer,
    geom public.geometry,
    CONSTRAINT enforce_dims_geom CHECK ((public.st_ndims(geom) = 2)),
    CONSTRAINT enforce_srid_geom CHECK ((public.st_srid(geom) = 4326))
);


ALTER TABLE mineturer.tracks OWNER TO mineturer2;

--
-- Name: tracks_trackid_seq; Type: SEQUENCE; Schema: mineturer; Owner: mineturer2
--

CREATE SEQUENCE tracks_trackid_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE mineturer.tracks_trackid_seq OWNER TO mineturer2;

--
-- Name: tracks_trackid_seq; Type: SEQUENCE OWNED BY; Schema: mineturer; Owner: mineturer2
--

ALTER SEQUENCE tracks_trackid_seq OWNED BY tracks.trackid;


--
-- Name: trips; Type: TABLE; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

CREATE TABLE trips (
    tripid integer NOT NULL,
    userid integer,
    title character varying,
    description text,
    start timestamp without time zone,
    stop timestamp without time zone,
    triptype character varying(50),
    flickrtags character varying(255)
);


ALTER TABLE mineturer.trips OWNER TO mineturer2;

--
-- Name: trips_tripid_seq; Type: SEQUENCE; Schema: mineturer; Owner: mineturer2
--

CREATE SEQUENCE trips_tripid_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE mineturer.trips_tripid_seq OWNER TO mineturer2;

--
-- Name: trips_tripid_seq; Type: SEQUENCE OWNED BY; Schema: mineturer; Owner: mineturer2
--

ALTER SEQUENCE trips_tripid_seq OWNED BY trips.tripid;


--
-- Name: userRoles; Type: TABLE; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

CREATE TABLE "userRoles" (
    userid integer NOT NULL,
    authority character varying(50) NOT NULL
);


ALTER TABLE mineturer."userRoles" OWNER TO mineturer2;

--
-- Name: users; Type: TABLE; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

CREATE TABLE users (
    userid integer NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    enabled boolean NOT NULL,
    email character varying(255),
    fullname character varying(255),
    flickrid character varying(50)
);


ALTER TABLE mineturer.users OWNER TO mineturer2;

--
-- Name: users_userid_seq; Type: SEQUENCE; Schema: mineturer; Owner: mineturer2
--

CREATE SEQUENCE users_userid_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE mineturer.users_userid_seq OWNER TO mineturer2;

--
-- Name: users_userid_seq; Type: SEQUENCE OWNED BY; Schema: mineturer; Owner: mineturer2
--

ALTER SEQUENCE users_userid_seq OWNED BY users.userid;


--
-- Name: waypoints; Type: TABLE; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

CREATE TABLE waypoints (
    wpid integer NOT NULL,
    tripid integer,
    geom public.geometry,
    CONSTRAINT enforce_dims_geom CHECK ((public.st_ndims(geom) = 2)),
    CONSTRAINT enforce_srid_geom CHECK ((public.st_srid(geom) = 4326))
);


ALTER TABLE mineturer.waypoints OWNER TO mineturer2;

--
-- Name: waypoints_wpid_seq; Type: SEQUENCE; Schema: mineturer; Owner: mineturer2
--

CREATE SEQUENCE waypoints_wpid_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE mineturer.waypoints_wpid_seq OWNER TO mineturer2;

--
-- Name: waypoints_wpid_seq; Type: SEQUENCE OWNED BY; Schema: mineturer; Owner: mineturer2
--

ALTER SEQUENCE waypoints_wpid_seq OWNED BY waypoints.wpid;


--
-- Name: pid; Type: DEFAULT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE points ALTER COLUMN pid SET DEFAULT nextval('points_pid_seq'::regclass);


--
-- Name: routekid; Type: DEFAULT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE routes ALTER COLUMN routekid SET DEFAULT nextval('routes_routekid_seq'::regclass);


--
-- Name: trackid; Type: DEFAULT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE tracks ALTER COLUMN trackid SET DEFAULT nextval('tracks_trackid_seq'::regclass);


--
-- Name: tripid; Type: DEFAULT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE trips ALTER COLUMN tripid SET DEFAULT nextval('trips_tripid_seq'::regclass);


--
-- Name: userid; Type: DEFAULT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE users ALTER COLUMN userid SET DEFAULT nextval('users_userid_seq'::regclass);


--
-- Name: wpid; Type: DEFAULT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE waypoints ALTER COLUMN wpid SET DEFAULT nextval('waypoints_wpid_seq'::regclass);


--
-- Name: pk_userid; Type: CONSTRAINT; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT pk_userid PRIMARY KEY (userid);


--
-- Name: pk_username_authority; Type: CONSTRAINT; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

ALTER TABLE ONLY "userRoles"
    ADD CONSTRAINT pk_username_authority PRIMARY KEY (userid, authority);


--
-- Name: points_pkey; Type: CONSTRAINT; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

ALTER TABLE ONLY points
    ADD CONSTRAINT points_pkey PRIMARY KEY (pid);


--
-- Name: routes_pkey; Type: CONSTRAINT; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

ALTER TABLE ONLY routes
    ADD CONSTRAINT routes_pkey PRIMARY KEY (routekid);


--
-- Name: tracks_pkey; Type: CONSTRAINT; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

ALTER TABLE ONLY tracks
    ADD CONSTRAINT tracks_pkey PRIMARY KEY (trackid);


--
-- Name: trips_pkey; Type: CONSTRAINT; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

ALTER TABLE ONLY trips
    ADD CONSTRAINT trips_pkey PRIMARY KEY (tripid);


--
-- Name: waypoints_pkey; Type: CONSTRAINT; Schema: mineturer; Owner: mineturer2; Tablespace: 
--

ALTER TABLE ONLY waypoints
    ADD CONSTRAINT waypoints_pkey PRIMARY KEY (wpid);


--
-- Name: fk_userid; Type: FK CONSTRAINT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE ONLY "userRoles"
    ADD CONSTRAINT fk_userid FOREIGN KEY (userid) REFERENCES users(userid) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: points_tripid_fkey; Type: FK CONSTRAINT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE ONLY points
    ADD CONSTRAINT points_tripid_fkey FOREIGN KEY (tripid) REFERENCES trips(tripid) ON DELETE CASCADE;


--
-- Name: routes_tripid_fkey; Type: FK CONSTRAINT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE ONLY routes
    ADD CONSTRAINT routes_tripid_fkey FOREIGN KEY (tripid) REFERENCES trips(tripid) ON DELETE CASCADE;


--
-- Name: tracks_tripid_fkey; Type: FK CONSTRAINT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE ONLY tracks
    ADD CONSTRAINT tracks_tripid_fkey FOREIGN KEY (tripid) REFERENCES trips(tripid) ON DELETE CASCADE;


--
-- Name: trips_userid_fkey; Type: FK CONSTRAINT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE ONLY trips
    ADD CONSTRAINT trips_userid_fkey FOREIGN KEY (userid) REFERENCES users(userid) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: waypoints_tripid_fkey; Type: FK CONSTRAINT; Schema: mineturer; Owner: mineturer2
--

ALTER TABLE ONLY waypoints
    ADD CONSTRAINT waypoints_tripid_fkey FOREIGN KEY (tripid) REFERENCES trips(tripid) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

