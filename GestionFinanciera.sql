PGDMP  9    3                |            GestionFinanciera    16.4    16.4 1    "           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            #           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            $           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            %           1262    16723    GestionFinanciera    DATABASE     �   CREATE DATABASE "GestionFinanciera" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
 #   DROP DATABASE "GestionFinanciera";
                postgres    false            �            1259    16799    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            �            1259    16738 
   categorias    TABLE     �   CREATE TABLE public.categorias (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL,
    tipo character varying(50) NOT NULL
);
    DROP TABLE public.categorias;
       public         heap    postgres    false            �            1259    16737    categorias_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categorias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.categorias_id_seq;
       public          postgres    false    218            &           0    0    categorias_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.categorias_id_seq OWNED BY public.categorias.id;
          public          postgres    false    217            �            1259    16771    egresos    TABLE     �  CREATE TABLE public.egresos (
    codigo integer NOT NULL,
    idcategoria integer NOT NULL,
    legajousuario integer NOT NULL,
    descripcion character varying(255),
    fecha date DEFAULT CURRENT_DATE NOT NULL,
    hora time without time zone DEFAULT CURRENT_TIME NOT NULL,
    destinatario character varying(255),
    importe double precision NOT NULL,
    impuestos double precision,
    idmetodopago integer NOT NULL
);
    DROP TABLE public.egresos;
       public         heap    postgres    false            �            1259    16770    egresos_codigo_seq    SEQUENCE     �   CREATE SEQUENCE public.egresos_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.egresos_codigo_seq;
       public          postgres    false    224            '           0    0    egresos_codigo_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.egresos_codigo_seq OWNED BY public.egresos.codigo;
          public          postgres    false    223            �            1259    16752    ingresos    TABLE     @  CREATE TABLE public.ingresos (
    codigo integer NOT NULL,
    idcategoria integer NOT NULL,
    legajousuario integer NOT NULL,
    descripcion character varying(255),
    fecha date DEFAULT CURRENT_DATE NOT NULL,
    hora time without time zone DEFAULT CURRENT_TIME NOT NULL,
    importe double precision NOT NULL
);
    DROP TABLE public.ingresos;
       public         heap    postgres    false            �            1259    16751    ingresos_codigo_seq    SEQUENCE     �   CREATE SEQUENCE public.ingresos_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.ingresos_codigo_seq;
       public          postgres    false    222            (           0    0    ingresos_codigo_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.ingresos_codigo_seq OWNED BY public.ingresos.codigo;
          public          postgres    false    221            �            1259    16745 
   metodopago    TABLE     h   CREATE TABLE public.metodopago (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL
);
    DROP TABLE public.metodopago;
       public         heap    postgres    false            �            1259    16744    metodopago_id_seq    SEQUENCE     �   CREATE SEQUENCE public.metodopago_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.metodopago_id_seq;
       public          postgres    false    220            )           0    0    metodopago_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.metodopago_id_seq OWNED BY public.metodopago.id;
          public          postgres    false    219            �            1259    16725    usuarios    TABLE     @  CREATE TABLE public.usuarios (
    legajo integer NOT NULL,
    nombre character varying(255) NOT NULL,
    dni character varying(20) NOT NULL,
    usuario character varying(255) NOT NULL,
    contrasena character varying(255) NOT NULL,
    nrocuenta double precision,
    tipo_usuario character varying(50) NOT NULL
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            �            1259    16724    usuarios_legajo_seq    SEQUENCE     �   CREATE SEQUENCE public.usuarios_legajo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.usuarios_legajo_seq;
       public          postgres    false    216            *           0    0    usuarios_legajo_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.usuarios_legajo_seq OWNED BY public.usuarios.legajo;
          public          postgres    false    215            i           2604    16741    categorias id    DEFAULT     n   ALTER TABLE ONLY public.categorias ALTER COLUMN id SET DEFAULT nextval('public.categorias_id_seq'::regclass);
 <   ALTER TABLE public.categorias ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            n           2604    16774    egresos codigo    DEFAULT     p   ALTER TABLE ONLY public.egresos ALTER COLUMN codigo SET DEFAULT nextval('public.egresos_codigo_seq'::regclass);
 =   ALTER TABLE public.egresos ALTER COLUMN codigo DROP DEFAULT;
       public          postgres    false    223    224    224            k           2604    16755    ingresos codigo    DEFAULT     r   ALTER TABLE ONLY public.ingresos ALTER COLUMN codigo SET DEFAULT nextval('public.ingresos_codigo_seq'::regclass);
 >   ALTER TABLE public.ingresos ALTER COLUMN codigo DROP DEFAULT;
       public          postgres    false    222    221    222            j           2604    16748    metodopago id    DEFAULT     n   ALTER TABLE ONLY public.metodopago ALTER COLUMN id SET DEFAULT nextval('public.metodopago_id_seq'::regclass);
 <   ALTER TABLE public.metodopago ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            h           2604    16728    usuarios legajo    DEFAULT     r   ALTER TABLE ONLY public.usuarios ALTER COLUMN legajo SET DEFAULT nextval('public.usuarios_legajo_seq'::regclass);
 >   ALTER TABLE public.usuarios ALTER COLUMN legajo DROP DEFAULT;
       public          postgres    false    215    216    216                      0    16799    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    225   
9                 0    16738 
   categorias 
   TABLE DATA           6   COPY public.categorias (id, nombre, tipo) FROM stdin;
    public          postgres    false    218   '9                 0    16771    egresos 
   TABLE DATA           �   COPY public.egresos (codigo, idcategoria, legajousuario, descripcion, fecha, hora, destinatario, importe, impuestos, idmetodopago) FROM stdin;
    public          postgres    false    224   �9                 0    16752    ingresos 
   TABLE DATA           i   COPY public.ingresos (codigo, idcategoria, legajousuario, descripcion, fecha, hora, importe) FROM stdin;
    public          postgres    false    222   �9                 0    16745 
   metodopago 
   TABLE DATA           0   COPY public.metodopago (id, nombre) FROM stdin;
    public          postgres    false    220   �9                 0    16725    usuarios 
   TABLE DATA           e   COPY public.usuarios (legajo, nombre, dni, usuario, contrasena, nrocuenta, tipo_usuario) FROM stdin;
    public          postgres    false    216   &:       +           0    0    categorias_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categorias_id_seq', 5, true);
          public          postgres    false    217            ,           0    0    egresos_codigo_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.egresos_codigo_seq', 1, false);
          public          postgres    false    223            -           0    0    ingresos_codigo_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.ingresos_codigo_seq', 1, false);
          public          postgres    false    221            .           0    0    metodopago_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.metodopago_id_seq', 4, true);
          public          postgres    false    219            /           0    0    usuarios_legajo_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.usuarios_legajo_seq', 1, false);
          public          postgres    false    215            �           2606    16803 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    225            x           2606    16743    categorias categorias_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.categorias DROP CONSTRAINT categorias_pkey;
       public            postgres    false    218            ~           2606    16780    egresos egresos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.egresos
    ADD CONSTRAINT egresos_pkey PRIMARY KEY (codigo);
 >   ALTER TABLE ONLY public.egresos DROP CONSTRAINT egresos_pkey;
       public            postgres    false    224            |           2606    16759    ingresos ingresos_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.ingresos
    ADD CONSTRAINT ingresos_pkey PRIMARY KEY (codigo);
 @   ALTER TABLE ONLY public.ingresos DROP CONSTRAINT ingresos_pkey;
       public            postgres    false    222            z           2606    16750    metodopago metodopago_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.metodopago
    ADD CONSTRAINT metodopago_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.metodopago DROP CONSTRAINT metodopago_pkey;
       public            postgres    false    220            r           2606    16734    usuarios usuarios_dni_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_dni_key UNIQUE (dni);
 C   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_dni_key;
       public            postgres    false    216            t           2606    16732    usuarios usuarios_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (legajo);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public            postgres    false    216            v           2606    16736    usuarios usuarios_usuario_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_usuario_key UNIQUE (usuario);
 G   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_usuario_key;
       public            postgres    false    216            �           2606    16781    egresos fk_egreso_categoria    FK CONSTRAINT     �   ALTER TABLE ONLY public.egresos
    ADD CONSTRAINT fk_egreso_categoria FOREIGN KEY (idcategoria) REFERENCES public.categorias(id);
 E   ALTER TABLE ONLY public.egresos DROP CONSTRAINT fk_egreso_categoria;
       public          postgres    false    224    218    4728            �           2606    16791    egresos fk_egreso_metodopago    FK CONSTRAINT     �   ALTER TABLE ONLY public.egresos
    ADD CONSTRAINT fk_egreso_metodopago FOREIGN KEY (idmetodopago) REFERENCES public.metodopago(id);
 F   ALTER TABLE ONLY public.egresos DROP CONSTRAINT fk_egreso_metodopago;
       public          postgres    false    4730    224    220            �           2606    16786    egresos fk_egreso_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY public.egresos
    ADD CONSTRAINT fk_egreso_usuario FOREIGN KEY (legajousuario) REFERENCES public.usuarios(legajo);
 C   ALTER TABLE ONLY public.egresos DROP CONSTRAINT fk_egreso_usuario;
       public          postgres    false    4724    224    216            �           2606    16760    ingresos fk_ingreso_categoria    FK CONSTRAINT     �   ALTER TABLE ONLY public.ingresos
    ADD CONSTRAINT fk_ingreso_categoria FOREIGN KEY (idcategoria) REFERENCES public.categorias(id);
 G   ALTER TABLE ONLY public.ingresos DROP CONSTRAINT fk_ingreso_categoria;
       public          postgres    false    4728    218    222            �           2606    16765    ingresos fk_ingreso_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY public.ingresos
    ADD CONSTRAINT fk_ingreso_usuario FOREIGN KEY (legajousuario) REFERENCES public.usuarios(legajo);
 E   ALTER TABLE ONLY public.ingresos DROP CONSTRAINT fk_ingreso_usuario;
       public          postgres    false    4724    216    222                  x������ � �         U   x�3�t���M�+IL�<�9��5�(�8�ˈ3�(1�� ��$&f���S��p����sz�AL���Ԣ�����b�h� P"            x������ � �            x������ � �         P   x�3�I,�J-ITHIUH.:�2%�$��Y4���$��1gHQb^qZjQj^rf�BRb^rbQf"�	�kZjrIfY>W� ��            x������ � �     