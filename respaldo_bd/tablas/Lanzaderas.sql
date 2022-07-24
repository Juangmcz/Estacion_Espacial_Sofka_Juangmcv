""" Este es el script de creacion de la tabla Lanzaderas """

USE [Estacion_Espacial_Sofka]
GO

/****** Object:  Table [dbo].[Naves_Lanzaderas]    Script Date: 24/07/2022 5:49:18 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Naves_Lanzaderas](
	[Id] [int] IDENTITY(0,1) NOT NULL,
	[Nombre] [varchar](20) NOT NULL,
	[Pais] [varchar](30) NOT NULL,
	[Peso] [float] NOT NULL,
	[Velocidad] [float] NOT NULL,
	[Altura] [float] NOT NULL,
	[Potencia] [float] NOT NULL,
	[Carga_Util] [float] NOT NULL,
	[Autonomia] [float] NOT NULL,
	[Combustible] [varchar](30) NOT NULL,
	[Anio] [int] NOT NULL,
 CONSTRAINT [Naves_Lanzaderas_PK] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO