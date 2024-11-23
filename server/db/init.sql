\connect grid_tracfin_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: designated_person; Type: TABLE; Schema: public; Owner: database_user
--

CREATE TABLE public.designated_person (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lastname character varying(50) NOT NULL,
    firstname character varying(50) NOT NULL
);

--
-- PostgreSQL database dump complete
--