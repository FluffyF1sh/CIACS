import json
import psycopg2


class ReadJson:
    clients = open('clients.json')
    clist = json.load(clients)
    ip_conn = clist['ip']
    file = open('fileProj.json')
    output = json.load(file)

    os = output['os']
    OS = os['name'], os['build'], os['bits']
    id = 6
    hardware = output['hardware']
    motherboards = hardware['motherboards']
    for item in motherboards:
        MotherBoard = item['manufacturer'], item['name']
    cpus = hardware['cpus']
    for item in cpus:
        CPU = item['manufacturer'], item['name'], item['cores'], item['threads'], item['speed'], item['bits']
    gpus = hardware['gpus']
    for item in gpus:
        GPU = item['manufacturer'], item['name'], item['capacity']
    rams = hardware['rams']
    for item in rams:
        RAM = item['manufacturer'], item['name'], item['type'], item['capacity']
    disks = hardware['disks']
    for item in disks:
        Disk = item['type'], item['capacity']
    software = output['software']
    for item in software:
        Software = item['name'], item['version']
    Hardware = MotherBoard, CPU, GPU, RAM, Disk

    Computer = id, ip_conn, OS, Hardware, Software

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1010",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="db")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        # tables = cursor.fetchall()

        # Computers

        cursor.execute("""INSERT INTO public.reports_computers (id, computer_id, ip)
                VALUES  (%s, %s, %s);
            """, (id, Computer[0], Computer[1]))

        # OS

        cursor.execute("""INSERT INTO public.reports_os (name, build, bits, computer_id_id)
                VALUES  (%s, %s, %s, %s);
            """, ((OS[0], OS[1], OS[2], id)))

        # Motherboards

        cursor.execute("""INSERT INTO public.reports_motherboards (manufacturer, name,computer_id_id)
                VALUES  (%s, %s, %s);
            """, ((MotherBoard[0], MotherBoard[1], id)))

        # CPUS

        cursor.execute("""
            INSERT INTO public.reports_cpus (manufacturer, name, cores, threads, speed, bits, computer_id_id)
                VALUES  (%s, %s, %s, %s, %s, %s, %s);
            """, ((CPU[0], CPU[1], CPU[2], CPU[3], CPU[4], CPU[5], id)))

        # GPUS

        cursor.execute("""
            INSERT INTO public.reports_gpus (manufacturer, name, capacity, computer_id_id)
                VALUES  (%s, %s, %s, %s);
            """, ((GPU[0], GPU[1], GPU[2], id)))

        # RAMS
        for ram in rams:
            cursor.execute("""
            INSERT INTO public.reports_rams (manufacturer, name, type, capacity, computer_id_id)
                VALUES  (%s, %s, %s, %s, %s);
            """, ((ram['manufacturer'], ram['name'], ram['type'], ram['capacity'], id)))

        # DISKS

        cursor.execute("""
            INSERT INTO public.reports_disks (type, capacity, computer_id_id)
                VALUES  (%s, %s, %s);
            """, ((Disk[0], Disk[1], id)))

        # Software

        for soft in software:
            cursor.execute("""
                INSERT INTO public.reports_software (name, version, computer_id_id)
                    VALUES  (%s, %s, %s);
            """, (soft['name'], soft['version'], id))

        connection.commit()
        print('PC configuration of {0}'.format(ip_conn) + ' is written to database with id {0}'.format(id))
        id += 1
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
