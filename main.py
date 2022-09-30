from pathlib import Path


# Given a laptop's "power" score, categorize into
# which third it falls: Lower End, Mid Range, or Top
# of the Line
def categorize(score, max_score, min_score):
    low_range = (max_score - min_score) * (1/3)
    mid_range = (max_score - min_score) * (2/3)
    if score < low_range:
        return "Lower End"
    elif score < mid_range:
        return "Mid Range"
    else:
        return "Top of the Line"


# Scale the given value to between 1 and 10
def scale(old_max, old_min, old_value):
    new_max = 10
    new_min = 1
    old_range = (old_max - old_min)
    if old_range == 0:
        # Don't divide by zero! Just return max
        # if only one value in series
        return new_max
    else:
        new_range = (new_max - new_min)
        return (((old_value - old_min) * new_range) / old_range) + new_min


# Find the max and min of each laptop attribute sold in each month
def monthly_min_max():
    cols = ["month", "price", "screen", "battery", "ram", "proc", "wifi", "hd", "apps"]
    # mmm (monthly-min-max) is table of min/maxes
    # month price-min   price-max   screen-min  screen-max
    # 1     395         457         15          15
    # 2     417         467         15          17

    mmm = []
    for row in range(1, 14):
        month_row = []
        mmm.append(month_row)
        for col in range(0, len(cols)):
            if row == 1:
                if col == 0:
                    month_row.append(cols[col])
                else:
                    month_row.append(cols[col] + ".min")
                    month_row.append(cols[col] + ".max")
            else:
                if col == 0:
                    month_row.append(row - 1)
                else:
                    month_row.append(9999)  # default min
                    month_row.append(-9999)  # default max

    file_path = Path.cwd() / "LaptopSales.csv"

    with file_path.open() as laptop_sales:
        i = 0
        x = 0
        for line in laptop_sales.readlines():
            i += 1  # line number
            line = line.strip()
            vals = line.split(",")
            # using uncleaned data file, so skip rows with
            # missing date or price vals
            if i == 1 or vals[0] == "" or vals[4] == "":
                x += 1
            else:
                month = int(vals[0][:vals[0].index("/")])

                price = int(vals[4])
                mmm[month][1] = min(mmm[month][1], price)
                mmm[month][2] = max(mmm[month][2], price)
                screen = int(vals[5])
                mmm[month][3] = min(mmm[month][3], screen)
                mmm[month][4] = max(mmm[month][4], screen)
                battery = int(vals[6])
                mmm[month][5] = min(mmm[month][5], battery)
                mmm[month][6] = max(mmm[month][6], battery)
                ram = int(vals[7])
                mmm[month][7] = min(mmm[month][7], ram)
                mmm[month][8] = max(mmm[month][8], ram)
                proc = float(vals[8])
                mmm[month][9] = min(mmm[month][9], proc)
                mmm[month][10] = max(mmm[month][10], proc)
                wifi = 1 if (vals[9] == "Yes") else 0
                mmm[month][11] = min(mmm[month][11], wifi)
                mmm[month][12] = max(mmm[month][12], wifi)
                hd = int(vals[10])
                mmm[month][13] = min(mmm[month][13], hd)
                mmm[month][14] = max(mmm[month][14], hd)
                apps = 1 if (vals[11] == "Yes") else 0
                mmm[month][15] = min(mmm[month][15], apps)
                mmm[month][16] = max(mmm[month][16], apps)

    file_path_out = Path.cwd() / "monthly/LaptopSalesMinMax.csv"

    with file_path_out.open(mode="w") as out:
        for row in mmm:
            print(row)
            out.write(",".join([str(num) for num in row]))
            out.write("\n")

    return mmm


# Same as monthly_min_max, but looks at the whole year instead of
# breaking out by month
def overall_min_max():
    cols = ["price", "screen", "battery", "ram", "proc", "wifi", "hd", "apps"]

    # omm (overall-min-max) is table of min/maxes
    # price-min   price-max   screen-min  screen-max
    # 395         457         15          15
    omm = []
    for row in range(0, 2):
        omm_row = []
        omm.append(omm_row)
        for col in range(0, len(cols)):
            if row == 0:
                omm_row.append(cols[col] + ".min")
                omm_row.append(cols[col] + ".max")
            else:
                omm_row.append(9999)  # default min
                omm_row.append(-9999)  # default max

    file_path = Path.cwd() / "LaptopSales.csv"

    with file_path.open() as laptop_sales:
        i = 0
        x = 0
        for line in laptop_sales.readlines():
            i += 1  # line number
            line = line.strip()
            vals = line.split(",")
            # using uncleaned data file, so skip rows with
            # missing date or price vals
            if i == 1 or vals[0] == "" or vals[4] == "":
                x += 1
            else:
                price = int(vals[4])
                omm[1][0] = min(omm[1][0], price)
                omm[1][1] = max(omm[1][1], price)
                screen = int(vals[5])
                omm[1][2] = min(omm[1][2], screen)
                omm[1][3] = max(omm[1][3], screen)
                battery = int(vals[6])
                omm[1][4] = min(omm[1][4], battery)
                omm[1][5] = max(omm[1][5], battery)
                ram = int(vals[7])
                omm[1][6] = min(omm[1][6], ram)
                omm[1][7] = max(omm[1][7], ram)
                proc = float(vals[8])
                omm[1][8] = min(omm[1][8], proc)
                omm[1][9] = max(omm[1][9], proc)
                wifi = 1 if (vals[9] == "Yes") else 0
                omm[1][10] = min(omm[1][10], wifi)
                omm[1][11] = max(omm[1][11], wifi)
                hd = int(vals[10])
                omm[1][12] = min(omm[1][12], hd)
                omm[1][13] = max(omm[1][13], hd)
                apps = 1 if (vals[11] == "Yes") else 0
                omm[1][14] = min(omm[1][14], apps)
                omm[1][15] = max(omm[1][15], apps)

    file_path_out = Path.cwd() / "overall/LaptopSalesMinMax.csv"

    with file_path_out.open(mode="w") as out:
        for row in omm:
            print(row)
            out.write(",".join([str(num) for num in row]))
            out.write("\n")

    return omm


# For each laptop, rescale each component 1-10 to reflect relative "power" to other
# laptops sold in the same month
def scaled_monthly_sales(mmm):
    # sc (scale) is table of each sale with laptop attributes scaled 1-10
    # and a total "power" rating that is the sum
    # month price       power   screen      battery     ram
    # 1     395         15.3    1           8.7         5.6
    # 2     417         17.7    10          5.4         2.3
    sc = []

    file_path = Path.cwd() / "LaptopSales.csv"

    with file_path.open() as laptop_sales:
        i = 0
        x = 0
        for line in laptop_sales.readlines():
            i += 1  # line number
            line = line.strip()
            vals = line.split(",")
            # using uncleaned data file, so skip rows with
            # missing date or price vals
            if i == 1 or vals[0] == "" or vals[4] == "":
                x += 1
            else:
                month = int(vals[0][:vals[0].index("/")])

                sc_row = []
                sc.append(sc_row)
                power = 0
                sc_row.append(month)

                price = int(vals[4])
                sc_row.append(price)

                screen = int(vals[5])
                minv = mmm[month][3]
                maxv = mmm[month][4]
                sc_val = scale(maxv, minv, screen)
                power += sc_val
                sc_row.append(sc_val)

                battery = int(vals[6])
                minv = mmm[month][5]
                maxv = mmm[month][6]
                sc_val = scale(maxv, minv, battery)
                power += sc_val
                sc_row.append(sc_val)

                ram = int(vals[7])
                minv = mmm[month][7]
                maxv = mmm[month][8]
                sc_val = scale(maxv, minv, ram)
                power += sc_val
                sc_row.append(sc_val)

                proc = float(vals[8])
                minv = mmm[month][9]
                maxv = mmm[month][10]
                sc_val = scale(maxv, minv, proc)
                power += sc_val
                sc_row.append(sc_val)

                wifi = 1 if (vals[9] == "Yes") else 0
                minv = mmm[month][11]
                maxv = mmm[month][12]
                sc_val = scale(maxv, minv, wifi)
                power += sc_val
                sc_row.append(sc_val)

                hd = int(vals[10])
                minv = mmm[month][13]
                maxv = mmm[month][14]
                sc_val = scale(maxv, minv, hd)
                power += sc_val
                sc_row.append(sc_val)

                apps = 1 if (vals[11] == "Yes") else 0
                minv = mmm[month][15]
                maxv = mmm[month][16]
                sc_val = scale(maxv, minv, apps)
                power += sc_val
                sc_row.append(sc_val)

                sc_row.insert(2, power)

    file_path_out = Path.cwd() / "monthly/LaptopSalesScaled.csv"

    with file_path_out.open(mode="w") as out:
        for row in sc:
            out.write(",".join([str(num) for num in row]))
            out.write("\n")

    return sc


# Sam as scaled_monthly_sales, but uses the min-max values
# for all laptops sold the whole year
def scaled_overall_sales(omm):
    # sc (scale) is table of each sale with laptop attributes scaled 1-10
    # and a total "power" rating that is the sum
    # month price       power   screen      battery     ram
    # 1     395         15.3    1           8.7         5.6
    # 2     417         17.7    10          5.4         2.3
    sc = []

    file_path = Path.cwd() / "LaptopSales.csv"

    with file_path.open() as laptop_sales:
        i = 0
        x = 0
        for line in laptop_sales.readlines():
            i += 1  # line number
            line = line.strip()
            vals = line.split(",")
            # using uncleaned data file, so skip rows with
            # missing date or price vals
            if i == 1 or vals[0] == "" or vals[4] == "":
                x += 1
            else:
                month = int(vals[0][:vals[0].index("/")])

                sc_row = []
                sc.append(sc_row)
                power = 0
                sc_row.append(month)

                price = int(vals[4])
                sc_row.append(price)

                screen = int(vals[5])
                minv = omm[1][2]
                maxv = omm[1][3]
                sc_val = scale(maxv, minv, screen)
                power += sc_val
                sc_row.append(sc_val)

                battery = int(vals[6])
                minv = omm[1][4]
                maxv = omm[1][5]
                sc_val = scale(maxv, minv, battery)
                power += sc_val
                sc_row.append(sc_val)

                ram = int(vals[7])
                minv = omm[1][6]
                maxv = omm[1][7]
                sc_val = scale(maxv, minv, ram)
                power += sc_val
                sc_row.append(sc_val)

                proc = float(vals[8])
                minv = omm[1][8]
                maxv = omm[1][9]
                sc_val = scale(maxv, minv, proc)
                power += sc_val
                sc_row.append(sc_val)

                wifi = 1 if (vals[9] == "Yes") else 0
                minv = omm[1][10]
                maxv = omm[1][11]
                sc_val = scale(maxv, minv, wifi)
                power += sc_val
                sc_row.append(sc_val)

                hd = int(vals[10])
                minv = omm[1][12]
                maxv = omm[1][13]
                sc_val = scale(maxv, minv, hd)
                power += sc_val
                sc_row.append(sc_val)

                apps = 1 if (vals[11] == "Yes") else 0
                minv = omm[1][14]
                maxv = omm[1][15]
                sc_val = scale(maxv, minv, apps)
                power += sc_val
                sc_row.append(sc_val)

                sc_row.insert(2, power)

    file_path_out = Path.cwd() / "overall/LaptopSalesScaled.csv"

    with file_path_out.open(mode="w") as out:
        for row in sc:
            out.write(",".join([str(num) for num in row]))
            out.write("\n")

    return sc


# Collects the min and max power of laptops sold in each month.
def monthly_power_min_max():
    # mpmm (monthly-power-min-max) is table of power min/maxes
    # month power-min   power-max
    # 1     43.561      67.999
    # 2     44.718      68.412
    mpmm = []
    mpmm.append(["month", "power-min", "power-max"])

    for month in range(1, 13):
        mpmm.append([1, 99999, -99999])  # default min/max

    file_path = Path.cwd() / "monthly/LaptopSalesScaled.csv"

    with file_path.open() as laptop_sales_scaled:
        for line in laptop_sales_scaled.readlines():
            line = line.strip()
            vals = line.split(",")

            month = int(vals[0])
            mpmm_row = mpmm[month]

            score = float(vals[2])
            mpmm_row[1] = min(mpmm_row[1], score)
            mpmm_row[2] = max(mpmm_row[2], score)

    file_path_out = Path.cwd() / "monthly/LaptopSalesScoreMinMax.csv"

    with file_path_out.open(mode="w") as out:
        for row in mpmm:
            out.write(",".join([str(num) for num in row]))
            out.write("\n")

    return mpmm


# Same as monthly_power_min_max but find the max/min score
# of all laptops sold that year
def overall_power_min_max():
    # opmm (overall-power-min-max) is table of power min/maxes
    # power-min   power-max
    # 43.561      67.999
    mpmm = []
    mpmm.append(["power-min", "power-max"])
    mpmm.append([99999, -99999])

    file_path = Path.cwd() / "overall/LaptopSalesScaled.csv"

    with file_path.open() as laptop_sales_scaled:
        for line in laptop_sales_scaled.readlines():
            line = line.strip()
            vals = line.split(",")

            score = float(vals[2])
            mpmm[1][0] = min(mpmm[1][0], score)
            mpmm[1][1] = max(mpmm[1][1], score)

    file_path_out = Path.cwd() / "overall/LaptopSalesScoreMinMax.csv"

    with file_path_out.open(mode="w") as out:
        for row in mpmm:
            # print(row)
            out.write(",".join([str(num) for num in row]))
            out.write("\n")

    return mpmm


# For each laptop, categorize as "Low Range", "Mid Range", or "Top of the Line"
# based on how much power it had versus other laptops sold that month
def categorized_monthly_sales(mpmm):
    # cat (categorized) is table of each sale with its power rating, category, and
    # power-per-dollar
    # month price       power   power-min   power-max   category    power-per-dollar
    # 1     395         15.3    43.561      67.999      Lower End   0.0387
    # 1     417         17.7    43.561      67.999      Mid Range   0.0424
    cat = []

    file_path = Path.cwd() / "monthly/LaptopSalesScaled.csv"

    with file_path.open() as laptop_sales_scaled:
        for line in laptop_sales_scaled.readlines():
            line = line.strip()
            vals = line.split(",")

            cat_row = []
            cat.append(cat_row)

            month = int(vals[0])
            cat_row.append(month)

            price = int(vals[1])
            cat_row.append(price)

            score = float(vals[2])
            cat_row.append(score)
            minv = mpmm[month][1]
            cat_row.append(minv)
            maxv = mpmm[month][2]
            cat_row.append(maxv)
            cat_row.append(categorize(score, maxv, minv))

            ppd = score / price
            cat_row.append(ppd)

    file_path_out = Path.cwd() / "monthly/LaptopSalesCategorized.csv"

    with file_path_out.open(mode="w") as out:
        for row in cat:
            out.write(",".join([str(num) for num in row]))
            out.write("\n")


# Same as categorized_monthly_sales, but uses the min/max
# scores of all laptops sold
def categorized_overall_sales(opmm):
    # cat (categorized) is table of each sale with its power rating, category, and
    # power-per-dollar
    # month price       power   power-min   power-max   category    power-per-dollar
    # 1     395         15.3    43.561      67.999      Lower End   0.0387
    # 1     417         17.7    43.561      67.999      Mid Range   0.0424
    cat = []

    file_path = Path.cwd() / "overall/LaptopSalesScaled.csv"

    with file_path.open() as laptop_sales_scaled:
        for line in laptop_sales_scaled.readlines():
            line = line.strip()
            vals = line.split(",")

            cat_row = []
            cat.append(cat_row)

            month = int(vals[0])
            cat_row.append(month)

            price = int(vals[1])
            cat_row.append(price)

            score = float(vals[2])
            cat_row.append(score)
            minv = opmm[1][0]
            cat_row.append(minv)
            maxv = opmm[1][1]
            cat_row.append(maxv)
            cat_row.append(categorize(score, maxv, minv))

            ppd = score / price
            cat_row.append(ppd)

    file_path_out = Path.cwd() / "overall/LaptopSalesCategorized.csv"

    with file_path_out.open(mode="w") as out:
        for row in cat:
            out.write(",".join([str(num) for num in row]))
            out.write("\n")


if __name__ == '__main__':
    mmm = monthly_min_max()
    sc = scaled_monthly_sales(mmm)
    mpmm = monthly_power_min_max()
    cat = categorized_monthly_sales(mpmm)
    # omm = overall_min_max()
    # sc = scaled_overall_sales(omm)
    # opmm = overall_power_min_max()
    # cat = categorized_overall_sales(opmm)


